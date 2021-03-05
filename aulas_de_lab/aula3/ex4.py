'''
Em álgebra linear, o produto escalar é uma função binária definida entre dois vetores que fornece um número real (também chamado "escalar") como resultado.
Algebricamente, o produto escalar de dois vetores é formado pela multiplicação de seus componentes correspondentes e pela soma dos produtos resultantes.

...

Faça um programa que leia a dimensão dos vetores a serem multiplicados, em seguida os componentes de cada vetor, e apresente como resultado o resultado escalar.

'''

a = []
b = []

print('Digite o vetor 1: ')
for n in range(3):
    n = int(input())
    a.append(n)

print('Digite o vetor 2: ')
for n in range(3):
    n = int(input())
    b.append(n)

dot_product = 0

for i in range(3):
    dot_product += (a[i]*b[i])

print(dot_product)