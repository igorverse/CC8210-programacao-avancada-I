'''

Exercício 02

a) Escreva uma função chamada par que receba um número e
retorne True se o número é par ou False caso contrário.

b) Escreva uma função lambda chamada par que receba um número
e retorne True se o número é par ou False caso contrário.

'''

# A)

def par(n):
    return (n % 2 == 0)

print(par(0))
print(par(15))
print(par(42))

# B)

parLambda = lambda n: n % 2 == 0

print(parLambda(0))
print(parLambda(15))
print(parLambda(42))

