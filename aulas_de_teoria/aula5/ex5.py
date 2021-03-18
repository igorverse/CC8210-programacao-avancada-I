'''
Exercício 05

Escreva uma função que receba uma lista de números e retorne o
maior e o menor número dessa lista.

'''

def higherAndLower(numbers):
    lower = numbers[0]
    higher = numbers[0]
    for n in numbers:
        if n > higher:
            higher = n
        if n < lower:
            lower = n
    return lower, higher

print(higherAndLower([1, 5, 78, 2, 0, -5, 42]))
print(higherAndLower([0, 9, 12, -15, 15, -42, 1]))
print(higherAndLower([10, 50, 78, 22, 0, 3, 4]))