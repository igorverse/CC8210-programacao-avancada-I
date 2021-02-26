'''
O ano é dividido em quatro estações: primavera, verão, outono e inverno. As datas exatas em que as estações mudam podem variar um pouco de ano para ano por causa da maneira que o calendário é construído. Neste exercício, usaremos as seguintes datas limites:

...

Crie um programa que recebe do usuário um mês e um dia. O usuário entrará o nome do mês como uma string, seguido do dia do mês como um inteiro. Então, seu programa deve exibir a estação associada à data que foi introduzida.
'''

day = int(input('Digite o dia desejado: '))
month = input('Digite o mês desejado: ')

if ((day >= 20 and month == 'março') or month == 'abril' or month == 'maio' or (month == 'junho' and day < 21)):
    print ('Outono')

elif ((day >= 21 and month == 'junho') or month == 'julho' or month == 'agosto' or (month == 'setembro' and day < 22)):
    print ('Inverno')

elif ((day >= 22 and month == 'setembro') or month == 'outubro' or month == 'novembro' or (month == 'dezembro' and day < 21)):
    print ('Primavera')

else: 
    print('Verão')
