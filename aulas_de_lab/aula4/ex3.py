'''
Faça um programa que multiplica duas matrizes de tamanho 3 x 3, sendo que a primeira matriz tem valores de 1 a 9, e a segunda deverá ser digitada pelo usuário.
'''

matrixA = []
user_matrix = []
final_matix = []

n = 0

for i in range(3):
    i = []
    for j in range(3):
        i.append((j+1)+n)
    matrixA.append(i)
    n += 3

for i in range(3):
    i = []
    for _ in range(3):
        i.append(int(input()))
    user_matrix.append(i)


adder = 0

for line in matrixA:
    b = []
    for x in range(3):
        for y in range(3):
            adder += line[y] * user_matrix[y][x]
        b.append(adder)
        adder = 0
    final_matix.append(b)

print(matrixA)
print(user_matrix)
print(final_matix)