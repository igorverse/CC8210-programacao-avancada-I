'''
Usando as bibliotecas Matplotlib e Pandas, faça um gráfico com o preço histórico do Ouro, com título, rótulos dos eixos e legenda.

Arquivo com o histórico do preço do ouro mensal: gold_prices_monthly.csv
'''

'''
Usando as bibliotecas Matplotlib e Pandas, faça um gráfico com o preço histórico do Ouro, com título, rótulos dos eixos e legenda.

Arquivo com o histórico do preço do ouro mensal: gold_prices_monthly.csv
'''

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("gold_prices_monthly.csv")

months_of_the_year = df["Date"]
price_of_the_month = df["Price"]

plt.plot(months_of_the_year, price_of_the_month, label="Variação do preço do ouro ao longo do tempo")
plt.title('Preço histórico do ouro')
plt.xlabel('Meses do ano')
plt.ylabel('Preço')
plt.xticks(range(1, len(months_of_the_year), 180))
plt.legend(loc="upper left")
plt.show()
