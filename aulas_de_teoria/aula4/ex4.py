'''
Faça um algoritmo que leia uma matriz M (populada com
números aleatórios) e exiba como saída o menor número
dessa matriz bem como o maior número.
'''

from random import randint

matrix = []
 
random_columns = randint(1, 10)

for i in range(randint(1, 10)):
    i = []
    for _ in range(random_columns):
        i.append(randint(1,100))
    matrix.append(i)

minA = matrix[0][0]

for line in matrix:
    for a in line:
        if (a < minA):
            minA = a
            
print(matrix)
print(minA)