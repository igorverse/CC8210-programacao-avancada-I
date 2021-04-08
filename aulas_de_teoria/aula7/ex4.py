'''

Escreva uma função que leia uma sequência numérica do arquivo “numeros3.txt” e
salva os números na lista num. Esta função deve retornar num. Escreva outra função
que recebe a lista num como parâmetro e retorna uma nova lista num_unicos, sem os
elementos repetidos. Escreva uma terceira função que recebe a lista num_unicos e
grava os números no arquivo “numeros3unicos.txt” 

'''

def numFile(filename):
    myFile = open(filename, 'r')
    numbers = "".join(myFile.readlines())
    num = numbers.split(' ')

    return num

def exclusiveNum(num):
    num_unicos = list(set(num))

    return num_unicos

def createFile(num_unicos):
    newFile = open('numeros3unicos.txt', 'w')
    numbers = " ".join(num_unicos)
    newFile.write(numbers)

    return 'Arquivo criado.'


print(numFile('numeros3.txt'))

print(exclusiveNum(numFile('numeros3.txt')))

print(createFile(exclusiveNum(numFile('numeros3.txt'))))

# Para observar o funcionamento, é necessário colocar o arquivo txt no diretório adequado.