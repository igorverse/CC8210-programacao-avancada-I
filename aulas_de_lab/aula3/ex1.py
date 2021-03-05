'''
O desvio padrão populacional é uma medida de dispersão em torno da média populacional de uma variável aleatória. 

O calculo do desvio padrão populacional pode ser calculado pela equação abaixo:

...

Onde: X é o vetor com os valores das amostras, e mi é a média de X, N é a quantidade de amostras.

 A média pode ser calculada pela equação abaixo:

...

Faça um programa que calcule a média e o desvio padrão de um vetor de 5 elementos definido pelo usuário.

'''
from math import sqrt

user_array = []
array_length = int(input('Qual o tamanho da lista: '))
print('Digite os valores: ')

for element in range(array_length):
    element = float(input())
    user_array.append(element)

array_sum = 0

for n in user_array:
    array_sum += n

average = array_sum / len(user_array)

deviation_sum = 0

for x in user_array:
    deviation_sum += (x - average)**2

standard_deviation = sqrt(deviation_sum / len(user_array))

print('Média = %.2f e Desvio = %.4f' %(average, standard_deviation))
