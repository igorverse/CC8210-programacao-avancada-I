'''
Faça um programa que crie uma lista contendo listas, onde cada lista contem a sequência de Fibonacci, sempre iniciando em 0.

O usuário deverá informar a sequência desejada.

A Sequência de Fibonacci é uma sequência de números inteiros iniciada em 0, na qual cada termos subsequente corresponde à soma dos dois anteriores.
'''

user_input = int(input('Digite a sequência desejada: '))

fibonacci = []

counter = 0

for i in range(user_input):
    counter += 1
    i = []
    for j in range(counter):
        if (len(i) < 2):
            i.append(j)
        else:
            i.append(i[len(i)-1] + i[len(i)-2])

    fibonacci.append(i)

print(fibonacci)