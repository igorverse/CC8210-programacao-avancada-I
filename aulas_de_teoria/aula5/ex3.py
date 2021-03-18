'''
Exercício 03

a) Escreva uma função que receba com parâmetro a temperatura em graus
Fahrenheit (F) para o usuário. Então, converta e retorne a temperatura
em graus Celsius (C).

C = (5 * (F-32) / 9)

b) Escreva uma função lambda que receba com parâmetro a temperatura
em graus Fahrenheit (F) para o usuário. Então, converta e retorne a
temperatura em graus Celsius (C).

C = (5 * (F-32) / 9)

'''


# A)

def fToC(f):
    return (5 * (f-32)) / 9

print(fToC(32))
print(fToC(0))

# B)

fToCelsius = lambda f: (5 * (f-32)) / 9

print(fToCelsius(32))
print(fToCelsius(0))
