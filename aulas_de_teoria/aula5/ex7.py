'''
Escreva uma função que receba uma lista e remova todos os valores
duplicados e retorne a lista sem elementos duplicados. Porém a
função não deve alterar a lista que recebeu como parâmetro.
'''

def noDuplicate(lista):
    removeDuplicates = list(set(lista))

    return removeDuplicates

print(noDuplicate([1, 2, 1, 5, 3, 2, 4, 2, 10]))
print(noDuplicate(['igor', 'igor', 'davi', 'davi', 'pedro', 'pedro']))
print(noDuplicate([True, True, False, True, False]))