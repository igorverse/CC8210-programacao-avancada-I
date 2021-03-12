'''
Faça um programa que cria uma matriz M (5 x 10), sendo
que cada elemento é um inteiro gerado aleatoriamente.
Então, exiba a matriz completa e, na sequência, somente
os elementos da primeira coluna da matriz.
'''

from random import randint

matrix = []

for i in range(5):
    i = []
    for _ in range(10):
        i.append(randint(0,100))
    matrix.append(i)

print(matrix)

for i in matrix:
    print(i[0])
