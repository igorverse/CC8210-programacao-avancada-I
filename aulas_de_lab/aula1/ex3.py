'''
Faça um Programa que peça a temperatura em graus
Fahrenheit (F) para o usuário. Então, transforma e exibe a
temperatura em graus Celsius (C).

C = (5 * (F-32) / 9)
'''

temperature = int(input('Insira a temperatura em Fahrenheit (F): '))
temperature2Celsius = 5 * ((temperature-32) / 9)

print(temperature2Celsius)