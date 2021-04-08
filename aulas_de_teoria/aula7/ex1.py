'''

Faça um programa que cria uma arquivo chamado pares.txt. O arquivo deverá conter
números pares de 0 até 998.

'''

myFile = open('pares.txt', 'w')

for i in range(1000):
    if i % 2 == 0:
        myFile.write('%d\n' %i) 