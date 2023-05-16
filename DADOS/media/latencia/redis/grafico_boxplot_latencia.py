import pandas as pd
import matplotlib.pyplot as plt

# Leitura dos dados dos arquivos
data_apt = pd.read_csv("media_latencia_apt.csv")
data_curl = pd.read_csv("media_latencia_curl.csv")
data_ping = pd.read_csv("media_latencia_ping.csv")
data_wget = pd.read_csv("media_latencia_wget.csv")

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
apt_group1 = pd.to_numeric(group1_apt["media"], errors='coerce')
apt_group2 = pd.to_numeric(group2_apt["media"], errors='coerce')

curl_group1 = pd.to_numeric(group1_curl["media"], errors='coerce')
curl_group2 = pd.to_numeric(group2_curl["media"], errors='coerce')

ping_group1 = pd.to_numeric(group1_ping["media"], errors='coerce')
ping_group2 = pd.to_numeric(group2_ping["media"], errors='coerce')

wget_group1 = pd.to_numeric(group1_wget["media"], errors='coerce')
wget_group2 = pd.to_numeric(group2_wget["media"], errors='coerce')

# Criação do gráfico Boxplot
fig, ax = plt.subplots()

ax.boxplot([apt_group1, apt_group2, curl_group1, curl_group2, ping_group1, ping_group2, wget_group1, wget_group2])

ax.set_xticklabels(["Group 1 - APT", "Group 2 - APT", "Group 1 - CURL", "Group 2 - CURL", "Group 1 - PING", "Group 2 - PING", "Group 1 - WGET", "Group 2 - WGET"], rotation=0)


ax.set_title("Comparison of mean values between Groups 1 and 2")
ax.set_xlabel("The average of the values from the latency experiment groups.")
ax.set_ylabel("Mean value (seconds)")

# Adicionar texto no lado direito
#ax.text(1.05, 0.1, "The average of the values from the latency experiment groups.", rotation=90, ha='left', transform=ax.transAxes)

#ax.set_ylabel("The average of the values from the latency experiment groups.", rotation=0, ha="right")

fig.set_size_inches(1366/100, 682/100)

plt.savefig("media_boxplot_latencia.png",dpi=1024)

plt.show()
