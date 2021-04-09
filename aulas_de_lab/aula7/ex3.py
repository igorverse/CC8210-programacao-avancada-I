'''
Escreva uma função em Python chamada somatorio() que receba o nome de um arquivo e retorne a somatória de todos os números que estão armazenados no arquivo. Todos os números do arquivo estão na mesma e única linha, separados por espaço.
'''

def somatorio(filename):
    myFile = open(filename, 'r')
    numbers = "".join(myFile.readlines())
    listOfNumbers = numbers.split(' ')

    adder = 0

    for number in listOfNumbers:
        if number != "":
            adder += int(number)

    return adder
