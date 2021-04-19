'''

Faça uma função chamada converte() que recebe um dicionário e uma String contendo uma frase e retorne uma frase convertida em código morse.

Sua função deverá traduzir cada letra e número para o código Morse, deixando um espaço entre cada letra ou número. Sua função deverá ignorar qualquer caractere que não seja letra ou número.

O dicionário referente ao código Morse de cada letra e número será fornecido conforme tabela abaixo:
...


codigo_morse = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.'}
'''
codigo_morse = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.'}


def converte(dic, phrase):
    morse_phrase = ""
    for letter in phrase:
        if letter.isalnum() and (letter.upper() in dic):
                morse_phrase += dic[letter.upper()] + ' '

    
    return morse_phrase


print(converte(codigo_morse, 'Teste@42'))