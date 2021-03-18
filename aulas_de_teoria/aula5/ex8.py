'''
Escreva uma função que receba uma lista de números inteiros e
retorne duas listas, uma com os números pares e outra com os
números impares.
'''

def intNumbers(numbers_list):
    oddList = []
    pairList = []
    for n in numbers_list:
        if n % 2 == 0:
            pairList.append(n)
        else:
            oddList.append(n)

    return oddList, pairList


print(intNumbers([4, 6, 10, 15, 18]))
print(intNumbers([42, 61, 100, 15, 18, 60, 3]))