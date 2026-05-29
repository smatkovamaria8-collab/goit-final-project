import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import ScalarFormatter
sns.set_style("whitegrid")

data = pd.read_csv("internet_service_churn.csv")
print(data.head(10))
data = data.iloc[:, 1:]

# print(data["is_tv_subscriber"].describe())

# sns.countplot(x="is_tv_subscriber", hue="is_tv_subscriber", data=data, legend= True)
# plt.xlabel("Чи підписаний на телебачення", fontsize="medium", color="midnightblue")
# plt.ylabel("Кількість людей", fontsize="medium", color="midnightblue")
# plt.legend(["0 - без підписки", "1 - з підпискою"], fontsize=10)
# plt.show()

# print(data["is_movie_package_subscriber"].describe())

# sns.countplot(x="is_movie_package_subscriber", hue="is_movie_package_subscriber", data=data, legend= True)
# plt.xlabel("Чи підписаний на пакет фільмів", fontsize="medium", color="midnightblue")
# plt.ylabel("Кількість людей", fontsize="medium", color="midnightblue")
# plt.legend(["0 - без підписки", "1 - з підпискою"], fontsize=10)
# plt.show()

# print(data["subscription_age"].describe())

# sns.histplot(x = "subscription_age", data=data)
# plt.xlabel("Термін підписки", fontsize="medium", color="midnightblue")
# plt.ylabel("Кількість людей", fontsize="medium", color="midnightblue")
# plt.show()

# print(data["bill_avg"].describe())

# sns.histplot(x = "bill_avg", data=data)
# plt.xlabel("Середній рахунок", fontsize="medium", color="midnightblue")
# plt.ylabel("Кількість людей", fontsize="medium", color="midnightblue")
# plt.xlim(-10, 120) 
# plt.show()

# print(data["reamining_contract"].describe())

# sns.histplot(x = "reamining_contract", data=data)
# plt.xlabel("Термін контракту, що залишився", fontsize="medium", color="midnightblue")
# plt.ylabel("Кількість людей", fontsize="medium", color="midnightblue")
# plt.show()

# print(data["service_failure_count"].describe())

# sns.countplot(x="service_failure_count", data=data)
# plt.xlabel("Кількість збоїв у сервісі", fontsize="medium", color="midnightblue")
# plt.ylabel("Кількість людей", fontsize="medium", color="midnightblue")
# plt.show()

# print(data["download_avg"].describe())

# sns.histplot(x = "download_avg", data=data)
# plt.xlabel("Середня кількість завантажень", fontsize="medium", color="midnightblue")
# plt.ylabel("Кількість людей", fontsize="medium", color="midnightblue")
# plt.xlim(0, 600) 
# plt.show()

# print(data["upload_avg"].describe())

# sns.histplot(x = "upload_avg", data=data)
# plt.xlabel("Середня кількість вивантажень", fontsize="medium", color="midnightblue")
# plt.ylabel("Кількість людей", fontsize="medium", color="midnightblue")
# plt.xlim(0, 50) 
# plt.show()

# print(data["download_over_limit"].describe())

# sns.countplot(x="download_over_limit", data=data)
# plt.xlabel("Скачувань понад норму", fontsize="medium", color="midnightblue")
# plt.ylabel("Кількість людей", fontsize="medium", color="midnightblue")
# plt.show()

# print(data["churn"].describe())

# sns.countplot(x="churn", hue = "churn", data=data, legend=True)
# plt.xlabel("Дані про відток", fontsize="medium", color="midnightblue")
# plt.ylabel("Кількість людей", fontsize="medium", color="midnightblue")
# plt.legend(["0 - клієнт залишився", "1 - клієнт пішов"], fontsize=10)
# plt.show()

print(data.info())

correlation = data.corr()
print(correlation)