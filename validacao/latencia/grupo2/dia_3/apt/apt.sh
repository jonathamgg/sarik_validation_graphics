#!/bin/bash
#
#  SARIK - Métricas
#
#  SITE:          https://sarik.org
#  Autor:         Jonathan G.P. dos Santos
#  Manutenção:    Jonathan G.P. dos Santos
#
#
#--------------------------------------------------------------------------------------#
#Exemplo:
#
#      Access the director metricas/script-
#      Conceder permissão ao arquivo
#      chmo +x -R metricas/
#      Acesse a pasta metricas e execute o seguitne comando:
#      ./metricas-01.sh
#--------------------------------------------------------------------------------------#
#Histórico
#
#  v1.0 20/02/2023, Jonathan G.P. dos Santos
#      - Beta.
#--------------------------------------------------------------------------------------#
#Testado em:
#  bash 5.0.17
#
#
#--------------------------------------------------------------------------------------#
#Agradecimentos:
#
#
#   Dr. Vinícius Pereira Gonçalves  - Orientador do projeto
#   Dr. Geraldo Pereira Rocha Filho - Coorientador do projeto
#   Msc. Elivaldo Ribeiro De Santana
#   Luiz Eduardo Rodrigues Lima
#   Tainá N. S. Mour
#
#
#--------------------------------------------------------------------------------------#
# Especificando a namespace
namespace="vote"

# Coletando informações dos pods
#pods=$(kubectl get pods -n $namespace | awk '{if(NR>1)print $1}')
#echo $pods[3]
kubectl get pods -n $namespace | awk '{if(NR>1)print $1}' > ngetPods.txt

readarray pods < ngetPods.txt

###############################  VARIAVEIS GERAIS  ##################################

# IP DO CLUSTER PARA OS TESTES DE COMUNICACAO

CLUSTER_IP=$(kubectl describe services kubernetes | grep Endpoints: | awk '{print $NF}' | cut -d':' -f1)

IP_VOTE=$(minikube service --url vote -n $namespace)
IP_RESULT=$(minikube service --url result -n $namespace)

Group="Group 2"

# VARIAVEIS NECESSARIAS PARA O CALCULO DO TEMPO DE RESPOSTA.
# TEMPO_DE_RESPOTA_START
# TEMPO_DE_RESPOTA_FIM

# Cores das letras

BRANCO="\033[37;00m"
VERDE="\033[32;1m"
VERMELHO="\033[31;1m"

###############################    FIM VARIAVEIS   ##################################

 # criação do arquo geral da 1 metrica tempo de resposta

echo "Data; Group; Nome_POD; APT" > metricas_tempo_resposta.csv
echo "Data,Group,Nome_POD,APT" > metricas_para_calculo.csv

# Loop para percorrer cada pod
for pod in ${pods[@]}; do
    echo ""
    echo "O nome do pod e: $(echo -e ${VERMELHO} $pod) $(echo -e ${BRANCO})"
    echo ""
        # criação s arquivos do 1º expeimento

        echo "Data; Group; Nome_POD; APT" > metricas_tempo_resposta_pod_$pod.csv

	echo "Group,APT" > metricas_para_R_pod_$pod.csv

        for i in {1..30}
         do
		 echo "O nome do pod e: $(echo -e ${VERMELHO} $pod) $(echo -e ${BRANCO})"
		 echo "Esse e o loop: $(echo -e ${VERDE} $i) $(echo -e ${BRANCO})"
		 echo ""

           # Coletar o tempo de resposta dos seguintes comandos: ping, wget, curl e apt

           #####################################  APT  ################################

	   START=0
           END=0
           DIFFERENCE=0
           resultado=0
           latencia=0
           fator=100
           latencia_int=0

	   # obtendo horario inicio
           START=$(date +%T | sed 's/://g')

           # Verifica se o pod usa imagem Alpine
            if [[ $(kubectl exec -it $pod -n $namespace -- cat /etc/os-release | grep -c "Alpine") -ne 0 ]]; then
                # Usando o time para definir um limite de tempo em todos os comandos.
                #latencia=$(kubectl exec -it $pod -n $namespace -- time apk update 2>&1 | grep -E 'real' | awk '{print $3}' | cut -d's' -f1 | awk '{printf "%.2f", $0}')
                latencia=$(kubectl exec -it $pod -n $namespace -- time apk update 2>&1 | grep -E 'real' | awk '{print $3}'| sed 's/[^0-9.]//g')

            else
                # Usando o time para definir um limite de tempo em todos os comandos.
                latencia=$(kubectl exec -it $pod -n $namespace -- bash -c "time apt update" | grep -E 'real' | awk '{print $2}'| sed 's/[^0-9.]//g')
                #latencia=$(kubectl exec -it $pod -n $namespace -- bash -c "time apt update" 2>&1 | grep -E 'real' | awk '{print $2}' | sed 's/[^0-9.]//g' | awk '{printf "%.2f", $0}' )

            fi

           # obtendo horario fim
           END=$(date +%T | sed 's/://g')

           # calculando a diferenca
           DIFFERENCE=$(printf "%.2f" $(echo "$END - $START" | bc))

           #latencia_int=$(echo "${latencia/,/.} * $fator" | bc | cut -d '.' -f 1)

           #latencia_int=$(echo "scale=2; $latencia_int / $fator" | bc)

           # exibindo o resultado
           echo $latencia
           # concatenando os valores
	   RESULT_TR_APT=$(echo "$latencia")

           #####################################  APT  ################################
           ####################  SAIDA DOS RESULTADOS INDIVIDUAL ######################

           echo "$(date); $Group; $pod; $RESULT_TR_APT" >> metricas_tempo_resposta_pod_$pod.csv

	   echo "$Group,$RESULT_TR_APT" >> metricas_para_R_pod_$pod.csv


           #################### FIM SAIDA DOS RESULTADOS ##############################

           ####################  SAIDA DOS RESULTADOS GERAIS ######################

           echo "$(date); $Group; $pod; $RESULT_TR_APT" >> metricas_tempo_resposta.csv
	   
	   echo "$(date +%d-%m-%Y),$Group,$pod,$RESULT_TR_APT" >> metricas_para_calculo.csv
           
	   ####################  SAIDA DOS RESULTADOS GERAIS ######################

        done
done
