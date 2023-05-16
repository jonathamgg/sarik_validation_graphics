import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Leitura dos dados dos arquivos
data_db = pd.read_csv("media_tt_db.csv")
data_redis = pd.read_csv("media_tt_redis.csv")
data_result = pd.read_csv("media_tt_result.csv")
data_vote = pd.read_csv("media_tt_vote.csv")

# Seleção dos dados por grupo
group1_db = data_db[data_db["Group"] == "Group 1"]
group2_db = data_db[data_db["Group"] == "Group 2"]

group1_redis = data_redis[data_redis["Group"] == "Group 1"]
group2_redis = data_redis[data_redis["Group"] == "Group 2"]

group1_result = data_result[data_result["Group"] == "Group 1"]
group2_result = data_result[data_result["Group"] == "Group 2"]

group1_vote = data_vote[data_vote["Group"] == "Group 1"]
group2_vote = data_vote[data_vote["Group"] == "Group 2"]

# Conversão dos dados para numéricos
db_group1 = pd.to_numeric(group1_db["media"], errors='coerce')
db_group2 = pd.to_numeric(group2_db["media"], errors='coerce')

redis_group1 = pd.to_numeric(group1_redis["media"], errors='coerce')
redis_group2 = pd.to_numeric(group2_redis["media"], errors='coerce')

result_group1 = pd.to_numeric(group1_result["media"], errors='coerce')
result_group2 = pd.to_numeric(group2_result["media"], errors='coerce')

vote_group1 = pd.to_numeric(group1_vote["media"], errors='coerce')
vote_group2 = pd.to_numeric(group2_vote["media"], errors='coerce')

# Cálculo do erro padrão
db_group1_std = np.std(db_group1) / np.sqrt(len(db_group1))
db_group2_std = np.std(db_group2) / np.sqrt(len(db_group2))
redis_group1_std = np.std(redis_group1) / np.sqrt(len(redis_group1))
redis_group2_std = np.std(redis_group2) / np.sqrt(len(redis_group2))
result_group1_std = np.std(result_group1) / np.sqrt(len(result_group1))
result_group2_std = np.std(result_group2) / np.sqrt(len(result_group2))
vote_group1_std = np.std(vote_group1) / np.sqrt(len(vote_group1))
vote_group2_std = np.std(vote_group2) / np.sqrt(len(vote_group2))

# Criação do gráfico com barras de erro
fig, ax = plt.subplots()

x = ["Group 1 - APT", "Group 2 - APT", "Group 1 - CURL", "Group 2 - CURL", "Group 1 - PING", "Group 2 - PING", "Group 1 - WGET", "Group 2 - WGET"]
y = [db_group1.mean(), db_group2.mean(), redis_group1.mean(), redis_group2.mean(), result_group1.mean(), result_group2.mean(), vote_group1.mean(), vote_group2.mean()]

# Calculando o erro padrão

se_db_group1 = db_group1.sem()
se_db_group2 = db_group2.sem()

se_redis_group1 = redis_group1.sem()
se_redis_group2 = redis_group2.sem()

se_result_group1 = result_group1.sem()
se_result_group2 = result_group2.sem()

se_vote_group1 = vote_group1.sem()
se_vote_group2 = vote_group2.sem()

# Criação do gráfico

fig, ax = plt.subplots()

ax.bar(["Group 1 - db", "Group 2 - db", "Group 1 - redis", "Group 2 - redis", "Group 1 - result", "Group 2 - result", "Group 1 - vote", "Group 2 - vote"],
[db_group1.mean(), db_group2.mean(), redis_group1.mean(), redis_group2.mean(), result_group1.mean(), result_group2.mean(), vote_group1.mean(), vote_group2.mean()],
color=["red", "blue", "orange", "green", "purple", "brown", "pink", "gray"],
yerr=[se_db_group1, se_db_group2, se_redis_group1, se_redis_group2, se_result_group1, se_result_group2, se_vote_group1, se_vote_group2],
capsize=5)

ax.set_title("Comparison of mean values between Groups 1 and 2 with standard error")
ax.set_xlabel("The average of the values from the transmission rate experiment groups.")
ax.set_ylabel("Transmission rate metric with mean value in (seconds)")

fig.set_size_inches(1366/100, 782/100)

plt.savefig("media_transmissao_ep.png", dpi=1024)
plt.show()
