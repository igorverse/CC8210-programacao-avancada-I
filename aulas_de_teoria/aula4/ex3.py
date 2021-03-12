'''
Faça um programa que cria uma matriz M (10 x 10),
sendo que cada elemento é um inteiro gerado
aleatoriamente no intervalo [0, 10]. Então, exiba a matriz
completa e a quantidade de incidências do número 3
'''

from random import randint

matrix = []

for i in range(10):
    i = []
    for _ in range(10):
        i.append(randint(0,10))
    matrix.append(i)

print(matrix)

counter = 0

for line in matrix:
    for a in line:
        if a == 3:
            counter += 1

print(counter)
