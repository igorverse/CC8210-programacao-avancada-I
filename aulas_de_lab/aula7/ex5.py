'''
Python usa o caractere # para marcar o início de um comentário. O comentário termina no final da linha contendo o caractere #. Neste exercício, você criará um programa que removerá todos os comentários de um arquivo de origem do Python. Verifique cada linha no arquivo para determinar se um caractere # está presente. Nesse caso, seu programa deve remover todos os caracteres da linha que comece com # (ignoramos a situação em que o caractere de comentário ocorre dentro de uma string). Salve o arquivo modificado usando um novo nome que será inserido pelo usuário. O usuário também informará o nome do arquivo de entrada. 
'''

print('==============================\nNão coloque a extensão do arquivo! Apenas o nome!\n==============================\n')
filename = input('Insira o nome do arquivo que terá seus comentários removidos: ')
print(filename + '.py aberto' + '\n\n')
newFilename = input('Insira o nome do novo arquivo: ')

myFile = open(filename + '.py', 'r')
newFile = open(newFilename + '.py', 'w')
lines = ("".join(myFile.readlines())).split('\n')

for line in lines:
    if len(line) > 0:
        if not (line[0] == '#'):
            newFile.write(line + '\n')

print('\n***Comentários removidos com sucesso.***\n')
print('Novo código salvo em ' + newFilename + '.py')

myFile.close()
newFile.close()