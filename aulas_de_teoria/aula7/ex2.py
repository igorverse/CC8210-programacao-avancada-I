'''
Crie um programa que inverta a ordem das linhas do arquivo pares.txt. A primeira linha
deve conter o maior número e a última linha o menor. Salve o resultado em outro
arquivo, chamado pares_invertido.txt.
'''


myFile = open('pares.txt', 'r')
newFile = open('pares_ordenados.txt', 'w')

for line in myFile:
    newLine = str(1000-int(line))
    if newLine != str(1000):
        newFile.write(newLine + '\n')
