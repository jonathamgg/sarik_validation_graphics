#!/bin/bash


######################################## EXEMPLO DE USO #########################################


#           diretorio,comando,arquivo > enviar para pasta desejada com o nome e extensao csv
#./script_01.sh latencia curl redis.csv > media/latencia/redis/media_latencia_curl.csv


######################################## EXEMPLO DE USO #########################################


# Define o diretório que contém as pastas com os arquivos
diretorio=$1
comando=$2
arquivos=$3
# Percorre cada pasta dia_x dentro do diretório
for pasta in $(find "$diretorio" -type d -name "dia_*"); do
    # Verifica se a pasta contém o arquivo db.csv
    arquivo="$pasta/$comando/$arquivos"
    if [ -f "$arquivo" ]; then
        # Imprime o nome da pasta
        echo "=== $pasta ==="

        # Lê o arquivo CSV, ignora a primeira linha e filtra as linhas por grupo
        # Calcula a média da coluna APT para cada grupo
        cat "$arquivo" | tail -n +2 | awk -F ',' '{
            if ($1 == "Group 1") {
                sum1 += $2;
                count1++;
            } else if ($1 == "Group 2") {
                sum2 += $2;
                count2++;
            }
        } END {
            if (count1 > 0) {
                print "Média do Group 1: " sum1/count1;
            } else {
                print "Não há dados para o Group 1.";
            }

            if (count2 > 0) {
                print "Média do Group 2: " sum2/count2;
            } else {
                print "Não há dados para o Group 2.";
            }
        }'
    fi
done
