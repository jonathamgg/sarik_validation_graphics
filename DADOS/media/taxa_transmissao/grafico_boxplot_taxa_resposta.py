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

# Criação do gráfico Boxplot
fig, ax = plt.subplots()

ax.boxplot([db_group1, db_group2, redis_group1, redis_group2, result_group1, result_group2, vote_group1, vote_group2])

ax.set_xticklabels(["Group 1 - db", "Group 2 - db", "Group 1 - redis", "Group 2 - redis", "Group 1 - result", "Group 2 - result", "Group 1 - vote", "Group 2 - vote"], rotation=0)


ax.set_title("Comparison of mean values between Groups 1 and 2")
ax.set_xlabel("The average of the values from the transmission rate experiment groups.")
ax.set_ylabel("Mean value (seconds)")

# Adicionar texto no lado direito
#ax.text(1.05, 0.1, "The average of the values from the latency experiment groups.", rotation=90, ha='left', transform=ax.transAxes)

#ax.set_ylabel("The average of the values from the latency experiment groups.", rotation=0, ha="right")

fig.set_size_inches(1366/100, 682/100)

plt.savefig("media_boxplot_taxa_transmissao.png",dpi=1024)

plt.show()
