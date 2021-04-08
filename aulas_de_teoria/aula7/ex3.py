'''
Escreva uma função em Python para retornar a somatória de todos os números que
estão armazenados no arquivo “numeros2.txt”. Todos os números do arquivo estão na
mesma e única linha, separados por espaço. 
'''


def sumNumbers(filename):
    myFile = open(filename, 'r')
    numbers = "".join(myFile.readlines())
    listOfNumbers = numbers.split(' ')

    adder = 0

    for number in listOfNumbers:
        adder += int(number)

    return adder


print(sumNumbers('numeros2.txt'))

# Para observar o funcionamento, é necessário colocar o arquivo txt no diretório adequado.