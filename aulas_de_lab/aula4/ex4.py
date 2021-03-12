'''
Crie um programa que realize a soma de todos os elementos da diagonal principal de uma matriz 4 x 4, 5 x 5, etc, preenchida com números de 1 até o tamanho da matriz.
'''

matrix = []
matrix_length = int(input('Digite o tamanho da matriz: '))
n = 0

for i in range(matrix_length):
    i = []
    for j in range(matrix_length):
        i.append((j+1)+n)
    matrix.append(i)
    n += matrix_length

print(matrix)

adder = 0

for i in range(matrix_length):
    for j in range(matrix_length):
        if (i == j):
            adder += matrix[i][j]


print(adder)