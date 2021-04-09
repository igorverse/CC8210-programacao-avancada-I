'''
Crie uma função chamada file_info que receba o nome do arquivo e conte quantas linhas, palavras e caracteres existente no arquivo. A função deverá retornar os valores de quantidade de linhas, palavras e caracteres respectivamente.
'''

def file_info(filename):
    file = open(filename, 'r')

    lines = file.readlines()
    chars = "".join(lines)

    words = []

    for line in lines:
        words.append(line.split(' '))

    adderWords = 0

    for n in words:
        adderWords += len(n)

    return len(lines), adderWords, len(chars)
