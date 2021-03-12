'''
Crie 3 listas:

● Inteiros: a primeira lista com 10 números inteiros gerados aleatoriamente
● Reais: a segunda lista com 15 números reais gerados aleatoriamente
● Complexos: A quarta lista com 5 números complexos criados por você.

Então, adicione as 3 listas a uma lista única, chamada completa. Apague
todas as 3 listas originais. Acesse e mostre todos os elementos da lista
completa.
'''

from random import random, randint

int_array = []
real_array = []
complex_array = [1+1j, 2+5j, 3+7j, 15+23j, 0+5j]

for _ in range(10):
    int_array.append(randint(0,100))

for _ in range(15):
    real_array.append(random()*100)

full_array = [int_array, real_array, complex_array]

del(int_array, real_array, complex_array)

print(full_array)