'''
Usando as bibliotecas Matplotlib e Pandas, faça um gráfico comparando o 
preço mensal do ouro com o preço do primeiro dia do mês do histórico da bolsa de NY, 
com título, rótulos dos eixos e legenda, dos anos 2000 até 2015.
'''

import pandas as pd
import matplotlib.pyplot as plt

df_gold = pd.read_csv("gold_prices_monthly.csv")
df_stocks = pd.read_csv("SP500_prices_monthly.csv")

filtered_year_gold = (df_gold["Date"] >= '2000-01-01') & (df_gold["Date"] <= '2015-12-01')

filtered_years_stocks = (df_stocks["Date"] >= '2000-01') & (df_stocks["Date"] <= '2015-12')

df_filtered_stocks = df_stocks[filtered_years_stocks]
df_filtered_gold = df_gold[filtered_year_gold]

price_of_stocks = df_filtered_stocks["Price"]
price_of_gold = df_filtered_gold["Price"]

years = df_filtered_gold["Date"]

plt.plot(years, price_of_stocks, color = "r", label = 'preço das ações')
plt.legend(loc="upper left")

plt.plot(years, price_of_gold, color = "y", label = 'preço do ouro')
plt.legend(loc="upper left")

plt.title('Comparação entre preço do ouro e preço das ações')
plt.xlabel('Quantidade de meses')
plt.ylabel('Variação de preços')

plt.xticks(range(1, len(years), 30))

plt.show()
