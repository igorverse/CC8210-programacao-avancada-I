'''
Usando as bibliotecas Matplotlib e Pandas, faça um gráfico de barras 
com a média anual do preço histórico da bolsa de NY, com título, 
rótulos dos eixos e legenda, dos anos 2000 até 2010.
'''
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("SP500_prices_monthly.csv")

filtered_years = (df["Date"] >= '2000-01-01') & (df["Date"] <= '2010-12-01')

df_filtered = df[filtered_years]

means_of_price = []

initial_index = 0
final_index = 12
for _ in range(0, len(df_filtered), 12):
    means_of_price.append(df_filtered[initial_index:final_index]["Price"].mean())
    initial_index += 12
    final_index += 12

years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010]
print(means_of_price[10])

plt.bar(years, means_of_price, color = "g")
plt.legend("Y" )
plt.title('média anual do preço histórico da bolsa de NY')
plt.xlabel('Anos')
plt.ylabel('Média anual')
plt.show()

