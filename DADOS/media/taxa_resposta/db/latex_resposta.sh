#!/bin/bash

# Recebe o nome do arquivo como parâmetro
media_file=$1

# Cria um array com os nomes dos grupos
groups=("Group 1" "Group 2")

# Imprime o cabeçalho da tabela em formato LaTeX
echo "\begin{table}[h]"
echo "\centering"
echo "\label{tab:medias}"
echo "\renewcommand{\tabcolsep}{0.05 pt}"
echo "\begin{tabular}{|l|l|l|l|l|l|l|l|l|l|l|}"
echo "\hline"
echo "\multicolumn{11}{|c|}{The average of the response rate metric values from the apt experiment.}\\\\"
echo "\hline"
echo "Group & Day 1 & Day 2 & Day 3 & Day 4 & Day 5 & Day 6 & Day 7 & Day 8 & Day 9 & Day 10 \\\\"
echo "\hline"

# Itera sobre os grupos
for group in "${groups[@]}"
do
  # Imprime o nome do grupo em formato LaTeX
  echo -n "$group & "

  # Itera sobre os dias
  for i in {1..10}
  do
    # Obtém a média para o grupo e dia correspondentes
    group_media=$(grep "$group" "$media_file" | cut -d ',' -f 2 | sed -n "${i}p")

    # Imprime o valor da média para o grupo e dia correspondentes em formato LaTeX
    echo -n "$group_media & "
  done

  # Imprime uma quebra de linha em formato LaTeX para passar para o próximo grupo
  echo "\\\\"
  echo "\hline"
done

# Imprime o fim da tabela em formato LaTeX
echo "\end{tabular}"
echo "\end{table}"

