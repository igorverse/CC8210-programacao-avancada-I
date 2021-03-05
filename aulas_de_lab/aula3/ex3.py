'''

Faça um Programa que leia 20 números inteiros e armazene-os em uma lista. 
Armazene os números pares na lista par e os números ímpares na lista impar. 
Imprima as três listas no final.

'''
number_array = []

for number in range(20):
    number = int(input())
    number_array.append(number)

odd_array = [n for n in number_array if n % 2 != 0]
pair_array = [n for n in number_array if n % 2 == 0]

for i in range(len(number_array)):
    if i == len(number_array) - 1:
        print(number_array[i])
    else:
        print(number_array[i], end=" ")

for i in range(len(odd_array)):
    if i == len(odd_array) - 1:
        print(odd_array[i])
    else:
        print(odd_array[i], end=" ")

for i in range(len(pair_array)):
    if i == len(pair_array) - 1:
        print(pair_array[i])
    else:
        print(pair_array[i], end=" ")