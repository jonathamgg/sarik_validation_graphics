import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import sem, t

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

# Cálculo da média e do erro padrão para cada grupo
means = [db_group1.mean(), db_group2.mean(), redis_group1.mean(), redis_group2.mean(), result_group1.mean(), result_group2.mean(), vote_group1.mean(), vote_group2.mean()]

sems = [sem(db_group1), sem(db_group2), sem(redis_group1), sem(redis_group2), sem(result_group1), sem(result_group2), sem(vote_group1), sem(vote_group2)]

# Cálculo do intervalo de confiança de 95% para cada grupo
conf_intervals = []
for i in range(len(means)):
    conf_intervals.append(t.interval(0.95, len([db_group1, db_group2, redis_group1, redis_group2, result_group1, result_group2, vote_group1, vote_group2])-1, loc=means[i], scale=sems[i]))

# Criação do gráfico com barras de erro e intervalos de confiança
fig, ax = plt.subplots()

x = ["Group 1 - db", "Group 2 - db", "Group 1 - redis", "Group 2 - redis", "Group 1 - result", "Group 2 - result", "Group 1 - vote", "Group 2 - vote"]
y = [db_group1.mean(), db_group2.mean(), redis_group1.mean(), redis_group2.mean(), result_group1.mean(), result_group2.mean(), vote_group1.mean(), vote_group2.mean()]

err = [1.96 * db_group1.sem(), 1.96 * db_group2.sem(), 1.96 * redis_group1.sem(), 1.96 * redis_group2.sem(), 1.96 * result_group1.sem(), 1.96 * result_group2.sem(), 1.96 * vote_group1.sem(), 1.96 * vote_group2.sem()]

ax.bar(x, y, yerr=err, capsize=10, color=["red", "blue", "orange", "green", "purple", "brown", "pink", "gray"])

ax.set_title("Comparison of mean values between Groups 1 and 2 with 95% confidence intervals")
ax.set_xlabel("The average of the values from the transmission rate experiment groups.")
ax.set_ylabel("Transmission rate metric with mean value in (seconds)")

fig.set_size_inches(1366/100, 782/100)

plt.savefig("media_transmission_ic.png",dpi=1024)
plt.show()

