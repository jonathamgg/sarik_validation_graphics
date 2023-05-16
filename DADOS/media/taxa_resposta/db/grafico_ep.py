import pandas as pd
import numpy as np
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

# Cálculo do erro padrão
apt_group1_std = np.std(apt_group1) / np.sqrt(len(apt_group1))
apt_group2_std = np.std(apt_group2) / np.sqrt(len(apt_group2))
curl_group1_std = np.std(curl_group1) / np.sqrt(len(curl_group1))
curl_group2_std = np.std(curl_group2) / np.sqrt(len(curl_group2))
ping_group1_std = np.std(ping_group1) / np.sqrt(len(ping_group1))
ping_group2_std = np.std(ping_group2) / np.sqrt(len(ping_group2))
wget_group1_std = np.std(wget_group1) / np.sqrt(len(wget_group1))
wget_group2_std = np.std(wget_group2) / np.sqrt(len(wget_group2))

# Criação do gráfico com barras de erro
fig, ax = plt.subplots()

x = ["Group 1 - APT", "Group 2 - APT", "Group 1 - CURL", "Group 2 - CURL", "Group 1 - PING", "Group 2 - PING", "Group 1 - WGET", "Group 2 - WGET"]
y = [apt_group1.mean(), apt_group2.mean(), curl_group1.mean(), curl_group2.mean(), ping_group1.mean(), ping_group2.mean(), wget_group1.mean(), wget_group2.mean()]

# Calculando o erro padrão

se_apt_group1 = apt_group1.sem()
se_apt_group2 = apt_group2.sem()

se_curl_group1 = curl_group1.sem()
se_curl_group2 = curl_group2.sem()

se_ping_group1 = ping_group1.sem()
se_ping_group2 = ping_group2.sem()

se_wget_group1 = wget_group1.sem()
se_wget_group2 = wget_group2.sem()

# Criação do gráfico

fig, ax = plt.subplots()

ax.bar(["Group 1 - APT", "Group 2 - APT", "Group 1 - CURL", "Group 2 - CURL", "Group 1 - PING", "Group 2 - PING", "Group 1 - WGET", "Group 2 - WGET"],
[apt_group1.mean(), apt_group2.mean(), curl_group1.mean(), curl_group2.mean(), ping_group1.mean(), ping_group2.mean(), wget_group1.mean(), wget_group2.mean()],
color=["red", "blue", "orange", "green", "purple", "brown", "pink", "gray"],
yerr=[se_apt_group1, se_apt_group2, se_curl_group1, se_curl_group2, se_ping_group1, se_ping_group2, se_wget_group1, se_wget_group2],
capsize=5)

ax.set_title("Comparison of mean values between Groups 1 and 2 with standard error")
ax.set_xlabel("The average of the values from the response rate experiment groups.")
ax.set_ylabel("Response rate metric with mean value in (seconds)")

fig.set_size_inches(1366/100, 782/100)

plt.savefig("media_tr_ep.png", dpi=1024)
plt.show()
