#!/bin/bash

# juntando os dados de cada experimento em um so

caminho1=../../../validacao/taxa_transmissao/grupo1/dia_2
caminho2=../../../validacao/taxa_transmissao/grupo2/dia_2

# caminho dos pods
db=metricas_para_R_pod_db-684b9b49fd-s8h8b.csv
redis=metricas_para_R_pod_redis-67db9bd79b-vfkg5.csv
result=metricas_para_R_pod_result-77f68799c4-2p4sr.csv
vote=metricas_para_R_pod_vote-79787c6c8b-dbn8r.csv
work=metricas_para_R_pod_worker-78b9ff59fc-vg8bx.csv

# nome dos arquivos
db1=db
redis1=redis
result1=result
vote1=vote
work1=work

# criando o arquivo db
cp $caminho1/$db $db1.csv

cat $caminho2/$db >> $db1.csv

sed -i '32d' $db1.csv

#criando o arquivo redis
cp $caminho1/$redis $redis1.csv

cat $caminho2/$redis >> $redis1.csv

sed -i '32d' $redis1.csv

#criando o arquivo result 
cp $caminho1/$result $result1.csv

cat $caminho2/$result >> $result1.csv

sed -i '32d' $result1.csv

#criando o arquivo vote
cp $caminho1/$vote $vote1.csv

cat $caminho2/$vote >> $vote1.csv

sed -i '32d' $vote1.csv

#criando o arquivo work
cp $caminho1/$work $work1.csv

cat $caminho2/$work >> $work1.csv

sed -i '32d' $work1.csv
