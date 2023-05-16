#!/bin/bash

# Recebe o nome do arquivo como parâmetro
media_file=$1

# Cria um array com os nomes dos grupos
groups=("Group 1" "Group 2")

# Imprime o cabeçalho da tabela
echo "Group, Dia 1, Dia 2, Dia 3, Dia 4, Dia 5, Dia 6, Dia 7, Dia 8, Dia 9, Dia 10"

# Itera sobre os grupos
for group in "${groups[@]}"
do
  # Imprime o nome do grupo
  echo -n "$group, "

  # Itera sobre os dias
  for i in {1..10}
  do
    # Obtém a média para o grupo e dia correspondentes
    group_media=$(grep "$group" "$media_file" | cut -d ',' -f 2 | sed -n "${i}p")

    # Imprime o valor da média para o grupo e dia correspondentes
    echo -n "$group_media, "
  done

  # Imprime uma quebra de linha para passar para o próximo grupo
  echo ""
done

