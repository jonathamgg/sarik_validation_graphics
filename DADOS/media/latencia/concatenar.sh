#!/bin/bash

#########################  EXEMPLO DE USO  ##################################

# Copie o script para o local que se encontrar o arquivo a ser corrigido
# em seguida execute o script dessa forma, passando como parâmetro o nome do arquivo

# ./concatenar.sh media_latencia_ping.csv

# O arquivo será corrigido

#########################  EXEMPLO DE USO  ##################################

arquivo=$1

# Salva a saída do primeiro comando awk em uma variável
group1=$(awk '/Group 1:/ { print $0 }' "$arquivo")

# Salva a saída do segundo comando awk em uma variável
group2=$(awk '/Group 2:/ { print $0 }' "$arquivo")

# exclui as linhas especificadas no arquivo
sed -i '28d;25d;22d;19d;16d;13d;10d;7d;4d;1d' "$arquivo"

# remove o texto "Média do" de todas as instâncias do arquivo
sed -i 's/Média do //' "$arquivo"

# adiciona a saída do primeiro comando awk de volta ao arquivo
echo "$group1" | tee "$arquivo" >/dev/null

# adiciona a saída do segundo comando awk de volta ao arquivo
echo "$group2" | tee -a "$arquivo" >/dev/null

# remove o texto "Média do" de todas as instâncias do arquivo
sed -i 's/Média do //g' "$arquivo"

# add uma linha do inicio
sed -i '1i Group,media' "$arquivo"

# alterar o : por ,
sed -i 's/: /,/g' "$arquivo"
