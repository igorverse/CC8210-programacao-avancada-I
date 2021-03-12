'''
Faça um programa que cria uma matriz M (2 x 2), sendo
que cada elemento deve ser digitado pelo usuário. Então,
faça seu programa criar outra matriz, N, que é resultante
do cálculo da multiplicação de cada elemento de M pelo
maior elemento da própria matriz M.
'''

user_matrix = []

higherA = 0

for i in range(2):
    i = []
    for n in range(2):
        i.append(float(input()))
        if (i[n] > higherA):
            higherA = i[n]
    user_matrix.append(i)

n_matrix = []

for line in user_matrix:
    for a in line:
        n_matrix.append(a*higherA)


print(user_matrix)
print(higherA)
print(n_matrix)
