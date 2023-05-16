import pandas as pd
import matplotlib.pyplot as plt

# Leitura dos dados dos arquivos
data_apt = pd.read_csv("media_tr_apt.csv")
data_curl = pd.read_csv("media_tr_curl.csv")
data_ping = pd.read_csv("media_tr_ping.csv")
data_wget = pd.read_csv("media_tr_wget.csv")

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

# Criação do gráfico
fig, ax = plt.subplots()

x = ["Group 1 - APT", "Group 2 - APT", "Group 1 - CURL", "Group 2 - CURL", "Group 1 - PING", "Group 2 - PING", "Group 1 - WGET", "Group 2 - WGET"]
y = [apt_group1.mean(), apt_group2.mean(), curl_group1.mean(), curl_group2.mean(), ping_group1.mean(), ping_group2.mean(), wget_group1.mean(), wget_group2.mean()]

ax.barh(x, y, color=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f"])
plt.xlim([0, max(y) * 1.1])

for i, v in enumerate(y):
    ax.text(v + max(y) * 0.03, i, str(round(v, 2)) + " s")

ax.set_title("Comparison of mean values between Groups 1 and 2")
ax.set_xlabel("Mean value (seconds)")
ax.set_ylabel("The average of the values from the latency experiment groups.")

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

fig.set_size_inches(1366/100, 782/100)

plt.savefig("media_blockspot_taxa_resposta.png",dpi=1024)

plt.show()
