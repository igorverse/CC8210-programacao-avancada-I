'''
Faça um programa que cria uma matriz, A, 5 x 5 com números inteiros em sequência e, então, exiba a matriz transposta de A ( At  ). 

Determinar a transposta de uma matriz é reescrevê-la de forma que suas linhas e colunas troquem de posições ordenadamente, isto é, a primeira linha é reescrita como a primeira coluna, a segunda linha é reescrita como a segunda coluna e assim por diante, até que se termine de reescrever todas as linhas na forma de coluna.
'''

matrix = []
t_matrix = []

n = 0

for i in range(5):
    i = []
    for j in range(5):
        i.append((j+1)+n)
    matrix.append(i)
    n += 5

a = 0

for column in range(5):
    column = []
    for line in matrix:
        column.append(line[a])
    t_matrix.append(column)
    a += 1

print(matrix)
print(t_matrix)