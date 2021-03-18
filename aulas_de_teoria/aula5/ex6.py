'''
Exercício 06

Escreva uma função que receba um número inteiro e retorne o valor
desse número em binário e em hexadecimal.

'''

def binAndHex(int_decimal):
    return bin(int(int_decimal)), hex(int(int_decimal))


print(binAndHex(1))
print(binAndHex(15))
print(binAndHex(13))