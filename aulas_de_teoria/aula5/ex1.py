'''
Exercício 01
a) Escreva uma função com parâmetros que receba a base e a
altura de um triângulo e retorne sua área (A = base * altura / 2).
b) Escreva uma função lambda que receba a base e a altura de um
triângulo e retorne sua área (A = base * altura / 2).
'''

# A)

def area(b, h):
    return (b*h) / 2

print(area(5, 4))
print(area(3, 3))

# B)

area = lambda b, h: (b*h) / 2

print(area(5, 4))
print(area(3, 3))



