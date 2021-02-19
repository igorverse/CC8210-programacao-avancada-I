'''
Escreva um programa que pergunte a quantidade de km percorridos
por um carro alugado, assim como a quantidade de dias pelos quais o
carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa
R$ 60,00 por dia e R$ 0,15 por km rodado.

'''

km = float(input("Quantidade de km percorridos: "))
days = float(input("Quantidade de dias do aluguel do carro: "))
price = (60 * days) + (0.15 * km)

print(price)
