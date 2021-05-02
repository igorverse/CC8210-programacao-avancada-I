from random import randint as rt


letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'


def generateLetter():
    
    return [letters[rt(0, 25)] for _ in range(4)]

def generateNumber():

    return [numbers[rt(0, 8)] for _ in range(3)]

def mergeNumAndLetter(generated_letters, generated_numbers):

    placa = ''.join((generated_letters[0:3] + generated_numbers[0:1] + generated_letters[3:4] + generated_numbers[1:3]))


    return placa