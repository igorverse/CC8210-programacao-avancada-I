'''
Faça um algoritmo que leia 2 vetores A[10] e B[10].
A seguir, crie um vetor C que seja a intersecção de A com B
e mostre este vetor C.

Obs.: Intersecção é quando um valor estiver nos dois
vetores. Considere que não há elementos duplicados em
cada um dos vetores.
'''

a = [1, 4, 5, 6, 10, 15, 3, 42, 0, 11]
b = [3, 5, 6, 7, 8, 4, 12, 45, 19, 18]
c = []

for valor in a:
    if valor in b:
        c.append(valor)

print(c)