import pandas as pd
import matplotlib.pyplot as plt

# Leitura dos dados dos arquivos
data_apt = pd.read_csv("media_tt_db.csv")
data_curl = pd.read_csv("media_tt_redis.csv")
data_ping = pd.read_csv("media_tt_result.csv")
data_wget = pd.read_csv("media_tt_vote.csv")

# Seleção dos dados por grupo
group1_apt = data_apt[data_apt["Group"] == "Group 1"]
group2_apt = data_apt[data_apt["Group"] == "Group 2"]

group1_curl = data_curl[data_curl["Group"] == "Group 1"]
group2_curl = data_curl[data_curl["Group"] == "Group 2"]

group1_ping = data_ping[data_ping["Group"] == "Group 1"]
group2_ping = data_ping[data_ping["Group"] == "Group 2"]

group1_wget = data_wget[data_wget["Group"] == "Group 1"]
group2_wget = data_wget[data_wget["Group"] == "Group 2"]

# Conversão dos dados para numéricos
db_group1 = pd.to_numeric(group1_apt["media"], errors='coerce')
db_group2 = pd.to_numeric(group2_apt["media"], errors='coerce')

redis_group1 = pd.to_numeric(group1_curl["media"], errors='coerce')
redis_group2 = pd.to_numeric(group2_curl["media"], errors='coerce')

result_group1 = pd.to_numeric(group1_ping["media"], errors='coerce')
result_group2 = pd.to_numeric(group2_ping["media"], errors='coerce')

vote_group1 = pd.to_numeric(group1_wget["media"], errors='coerce')
vote_group2 = pd.to_numeric(group2_wget["media"], errors='coerce')

# Criação do gráfico
fig, ax = plt.subplots()

ax.bar(["Group 1 - db", "Group 2 - db", "Group 1 - redis", "Group 2 - redis", "Group 1 - result", "Group 2 - result", "Group 1 - vote", "Group 2 - vote"],
       [db_group1.mean(), db_group2.mean(), redis_group1.mean(), redis_group2.mean(), result_group1.mean(), result_group2.mean(), vote_group1.mean(), vote_group2.mean()],
       color=["red", "blue", "orange", "green", "purple", "brown", "pink", "gray"])

ax.set_title("Comparison of mean values between Groups 1 and 2")
ax.set_xlabel("The average of the values from the transmission rate experiment groups.")
ax.set_ylabel("Mean value (seconds)")

fig.set_size_inches(1366/100, 782/100)

plt.savefig("media_taxa_transmissao.png",dpi=1024)

plt.show()
