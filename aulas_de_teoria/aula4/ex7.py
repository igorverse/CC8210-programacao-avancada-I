'''
Dada uma matriz de tamanho 6 por 10. Pede
se:
Inicialize essa matriz com apenas 1 (um) e 0 (zero) (números
inteiros) aleatoriamente.
Inverta o conteúdo da matriz, ou seja, onde era 1 fica 0, e
onde era zero fica 1.
'''

from random import randint

matrixA = []
matrixB = []

for i in range(6):
    i = []
    for _ in range(10):
        i.append(randint(0,1))
    matrixA.append(i)

print(matrixA)

for line in matrixA:
    for a in line:
        if a == 0:
            a = 1
            matrixB.append(a)
        else:
            matrixB.append(0)

matrixA = matrixB
del(matrixB)

print('')
print(matrixA)