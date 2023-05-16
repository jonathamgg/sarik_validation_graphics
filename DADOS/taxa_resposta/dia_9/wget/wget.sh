#!/bin/bash

# juntando os dados de cada experimento em um so

caminho1=../../../../validacao/taxa_resposta/grupo1/dia_9
caminho2=../../../../validacao/taxa_resposta/grupo2/dia_9

# pasta experimento
comando=wget

# caminho dos pods 
db=metricas_para_R_pod_db-684b9b49fd-d6xt4.csv
redis=metricas_para_R_pod_redis-67db9bd79b-78588.csv
result=metricas_para_R_pod_result-77f68799c4-f8f44.csv
vote=metricas_para_R_pod_vote-79787c6c8b-vmbcs.csv
work=metricas_para_R_pod_worker-78b9ff59fc-22j4t.csv

# caminho dos pods
#db=
#redis=
#result=
#vote=
#work=

# nome dos arquivos
db1=db
redis1=redis
result1=result
vote1=vote
work1=work

# criando o arquivo db
cp $caminho1/$comando/$db $db1.csv

cat $caminho2/$comando/$db >> $db1.csv

sed -i '32d' $db1.csv

#criando o arquivo redis
cp $caminho1/$comando/$redis $redis1.csv

cat $caminho2/$comando/$redis >> $redis1.csv

sed -i '32d' $redis1.csv

#criando o arquivo result 
cp $caminho1/$comando/$result $result1.csv

cat $caminho2/$comando/$result >> $result1.csv

sed -i '32d' $result1.csv

#criando o arquivo vote
cp $caminho1/$comando/$vote $vote1.csv

cat $caminho2/$comando/$vote >> $vote1.csv

sed -i '32d' $vote1.csv

#criando o arquivo work
cp $caminho1/$comando/$work $work1.csv

cat $caminho2/$comando/$work >> $work1.csv

sed -i '32d' $work1.csv
