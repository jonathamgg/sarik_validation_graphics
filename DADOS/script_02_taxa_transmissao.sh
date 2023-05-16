#!/bin/bash

# Define o diretório que contém as pastas com os arquivos
diretorio=$1
arquivos=$2
# Percorre cada pasta dia_x dentro do diretório
for pasta in $(find "$diretorio" -type d -name "dia_*"); do
    # Verifica se a pasta contém o arquivo db.csv
    arquivo="$pasta/$arquivos"
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
