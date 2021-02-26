'''
O Máximo Divisor Comum (MDC) de dois números inteiros positivos, n e m, é o maior número, d, que divide de forma inteira n e m. Existem vários algoritmos que podem ser usados para resolver esse problema, incluindo: 

...

Escreva um programa que leia dois números inteiros positivos do usuário e use esse algoritmo para determinar e reportar seu maior divisor comum.

'''
n = int(input('Digite n: '))
m = int(input('Digite m: '))
d = 0

if m > n:
    d = n
else:
    d = m

while (m % d != 0) or (n % d != 0):
    d -= 1

print (d)
