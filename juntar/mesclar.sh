#!/bin/bash

# juntando os dados de cada experimento em um so

#pasta experimento
comando=wget

# criando o arquivo db
cp ..grupo1/$comando/metricas_para_R_pod_db-684b9b49fd-kcvsm.csv db.csv

cat ..grupo2/$comando/metricas_para_R_pod_db-684b9b49fd-kcvsm.csv >> db.csv

sed -i '12d' db.csv

cp db.csv db1.csv

sed -i 's/,/;/g' db1.csv

#criando o arquivo redis
cp ..grupo1/$comando/metricas_para_R_pod_redis-67db9bd79b-kr8wd.csv redis.csv

cat ..grupo2/$comando/metricas_para_R_pod_redis-67db9bd79b-kr8wd.csv >> redis.csv

sed -i '12d' redis.csv

cp redis.csv redis1.csv

sed -i 's/,/;/g' redis1.csv


#criando o arquivo result 
cp ..grupo1/$comando/metricas_para_R_pod_result-77f68799c4-5xt9s.csv result.csv

cat ..grupo2/$comando/metricas_para_R_pod_result-77f68799c4-5xt9s.csv >> result.csv

sed -i '12d' result.csv

cp result.csv result1.csv

sed -i 's/,/;/g' result1.csv

#criando o arquivo vote
cp ..grupo1/$comando/metricas_para_R_pod_vote-79787c6c8b-2mj4f.csv vote.csv

cat ..grupo2/$comando/metricas_para_R_pod_vote-79787c6c8b-2mj4f.csv >> vote.csv

sed -i '12d' vote.csv

cp vote.csv vote1.csv

sed -i 's/,/;/g' vote1.csv


#criando o arquivo work
cp ..grupo1/$comando/metricas_para_R_pod_worker-78b9ff59fc-rq4hs.csv worker.csv

cat ..grupo2/$comando/metricas_para_R_pod_worker-78b9ff59fc-rq4hs.csv >> worker.csv

sed -i '12d' worker.csv

cp worker.csv worker1.csv

sed -i 's/,/;/g' worker1.csv
