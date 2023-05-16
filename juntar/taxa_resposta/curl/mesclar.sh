#!/bin/bash

# juntando os dados de cada experimento em um so

#pasta experimento
comando=curl


#pods

db1=metricas_para_R_pod_db-684b9b49fd-lhb6h.csv
db2=metricas_para_R_pod_db-684b9b49fd-lhb6h.csv
redis1=metricas_para_R_pod_redis-67db9bd79b-m5dld.csv
redis2=metricas_para_R_pod_redis-67db9bd79b-m5dld.csv
result1=metricas_para_R_pod_result-77f68799c4-czkh9.csv
result2=metricas_para_R_pod_result-77f68799c4-czkh9.csv
vote1=metricas_para_R_pod_vote-79787c6c8b-n6rgl.csv
vote2=metricas_para_R_pod_vote-79787c6c8b-n6rgl.csv
work1=metricas_para_R_pod_worker-78b9ff59fc-zpghs.csv
work2=metricas_para_R_pod_worker-78b9ff59fc-zpghs.csv

# criando o arquivo db
cp ../../grupo1/$comando/$db1 db.csv

cat ../../grupo2/$comando/$db2 >> db.csv

sed -i '12d' db.csv

#cp db.csv db1.csv

#sed -i 's/,/;/g' db1.csv

#criando o arquivo redis
cp ../../grupo1/$comando/$redis1 redis.csv

cat ../../grupo2/$comando/$redis2 >> redis.csv

sed -i '12d' redis.csv

#cp redis.csv redis1.csv

#sed -i 's/,/;/g' redis1.csv


#criando o arquivo result 
cp ../../grupo1/$comando/$result1 result.csv

cat ../../grupo2/$comando/$result2 >> result.csv

sed -i '12d' result.csv

#cp result.csv result1.csv

#sed -i 's/,/;/g' result1.csv

#criando o arquivo vote
cp ../../grupo1/$comando/$vote1 vote.csv

cat ../../grupo2/$comando/$vote2 >> vote.csv

sed -i '12d' vote.csv

#cp vote.csv vote1.csv

#sed -i 's/,/;/g' vote1.csv


#criando o arquivo work
cp ../../grupo1/$comando/$work1 worker.csv

cat ../../grupo2/$comando/$work2 >> worker.csv

sed -i '12d' worker.csv

#cp worker.csv worker1.csv

#sed -i 's/,/;/g' worker1.csv
