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
#  v1.0 24/01/2023, Jonathan G.P. dos Santos
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

echo "Data; Group; Nome_POD; PING" > metricas_tempo_resposta.csv
echo "Data,Group,Nome_POD,PING" > metricas_para_calculo.csv

# Loop para percorrer cada pod
for pod in ${pods[@]}; do
    echo ""
    echo "O nome do pod e: $(echo -e ${VERMELHO} $pod) $(echo -e ${BRANCO})"
    echo ""
        # criação s arquivos do 1º expeimento

        echo "Data; Group; Nome_POD; PING" > metricas_tempo_resposta_pod_$pod.csv

	echo "Group,PING" > metricas_para_R_pod_$pod.csv

        for i in {1..30}
         do
		 echo "O nome do pod e: $(echo -e ${VERMELHO} $pod) $(echo -e ${BRANCO})"
		 echo "Esse e o loop: $(echo -e ${VERDE} $i) $(echo -e ${BRANCO})"
		 echo ""

           # Coletar o tempo de resposta dos seguintes comandos: ping, wget, curl e apt


           ####################################  PING ################################


	   START=""
           END=""
	   MS=""
	   DIFFERENCE=""
	   date_ini=""
	   date_fim=""
	   resultado=""
	   timeout=""
	   
	   # obtendo horario inicio
	   date_ini=$(date +%T | sed 's/://g')

	   # transformando em decimal
	   START=$((10#$date_ini))

           # Executando o comando ping.
           kubectl exec -it $pod -n $namespace -- ping -c 8 $CLUSTER_IP

	   # obtendo horario fim
   	   date_fim=$(date +%T | sed 's/://g')

	   # transformando em decimal
	   END=$((10#$date_fim))

	   # coletando o tempo em nano segundos
	   MS=$(date +%s.%N | sed 's/[^0-9.,]//g' | cut -c1-10)

	   # transformando em numero
	   MS=$(echo "$MS" | bc)

	   # calculando a diferenca
	   DIFFERENCE=$((END - START))

	   # deixando uma unica casa decimal sem numeros apos .
	   DIFFERENCE=$(echo "scale=2; $DIFFERENCE" | bc | awk '{printf "%.1f", $0}')

	   # concatenando os valores	   
	   RESULT_TR_PING=$(echo "$DIFFERENCE$MS" | bc)

           ####################################  PING ################################

           ####################  SAIDA DOS RESULTADOS INDIVIDUAL ######################

           echo "$(date); $Group; $pod; $RESULT_TR_PING" >> metricas_tempo_resposta_pod_$pod.csv

	   echo "$Group,$RESULT_TR_PING" >> metricas_para_R_pod_$pod.csv


           #################### FIM SAIDA DOS RESULTADOS ##############################

           ####################  SAIDA DOS RESULTADOS GERAIS ######################

           echo "$(date); $Group; $pod; $RESULT_TR_PING" >> metricas_tempo_resposta.csv
	   
	   echo "$(date +%d-%m-%Y),$Group,$pod,$RESULT_TR_PING" >> metricas_para_calculo.csv
           
	   ####################  SAIDA DOS RESULTADOS GERAIS ######################

        done
done
