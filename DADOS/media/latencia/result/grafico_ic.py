import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import sem, t

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

# Cálculo da média e do erro padrão para cada grupo
means = [apt_group1.mean(), apt_group2.mean(), curl_group1.mean(), curl_group2.mean(), ping_group1.mean(), ping_group2.mean(), wget_group1.mean(), wget_group2.mean()]

sems = [sem(apt_group1), sem(apt_group2), sem(curl_group1), sem(curl_group2), sem(ping_group1), sem(ping_group2), sem(wget_group1), sem(wget_group2)]

# Cálculo do intervalo de confiança de 95% para cada grupo
conf_intervals = []
for i in range(len(means)):
    conf_intervals.append(t.interval(0.95, len([apt_group1, apt_group2, curl_group1, curl_group2, ping_group1, ping_group2, wget_group1, wget_group2])-1, loc=means[i], scale=sems[i]))

# Criação do gráfico com barras de erro e intervalos de confiança
fig, ax = plt.subplots()

x = ["Group 1 - APT", "Group 2 - APT", "Group 1 - CURL", "Group 2 - CURL", "Group 1 - PING", "Group 2 - PING", "Group 1 - WGET", "Group 2 - WGET"]
y = [apt_group1.mean(), apt_group2.mean(), curl_group1.mean(), curl_group2.mean(), ping_group1.mean(), ping_group2.mean(), wget_group1.mean(), wget_group2.mean()]

err = [1.96 * apt_group1.sem(), 1.96 * apt_group2.sem(), 1.96 * curl_group1.sem(), 1.96 * curl_group2.sem(), 1.96 * ping_group1.sem(), 1.96 * ping_group2.sem(), 1.96 * wget_group1.sem(), 1.96 * wget_group2.sem()]

ax.bar(x, y, yerr=err, capsize=10, color=["red", "blue", "orange", "green", "purple", "brown", "pink", "gray"])

ax.set_title("Comparison of mean values between Groups 1 and 2 with 95% confidence intervals")
ax.set_xlabel("The average of the values from the latency experiment groups.")
ax.set_ylabel("Latency metric with mean value in (seconds)")

fig.set_size_inches(1366/100, 782/100)

plt.savefig("media_latencia_ic.png",dpi=1024)
plt.show()

