'''
Crie uma função em Python chamada maiorPalavra que recebe uma string e identifica a(s) palavra(s) mais longa(s) nessa string. Sua função deve retornar o tamanho da palavra mais longa e uma lista de todas as palavras desse comprimento que ocorreram na string, sem palavras repetidas.
'''

def maiorPalavra(string):
    words = string.replace(",", "").split(' ')
    higher_words = []
    words_no_repeat = []
    
    higher = len(words[0])

    for word in words:
        if len(word) >= higher:
            higher = len(word)

        if word not in words_no_repeat:
            words_no_repeat.append(word)

    for word in words_no_repeat:
        if len(word) == higher:
            higher_words.append(word)

    return higher, higher_words

print(maiorPalavra("A Maria ama laranja, abacaxi e uva, mas não gosta de suco de abacaxi"))

