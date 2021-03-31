'''
A Criptografia de César é uma técnica bastante simples e provavelmente a mais conhecida de todas.

Trata-se de um tipo de substituição, na qual cada letra de um texto a ser criptografado é substituída por outra letra presente no alfabeto, porém deslocada um certo número de posições à esquerda ou à direita.

Por exemplo, se empregarmos uma troca de quatro posições à esquerda, cada letra é substituída pela letra que está quatro posições adiante no alfabeto, e nesse caso a letra A seria substituída pela letra E, a letra B por F, a letra C por G, e assim sucessivamente.

Crie uma função chamada criptCesar que receba uma frase e o valor do deslocamento, podendo ser positivo ou negativo. A criptografia deverá ser cíclica, como na imagem acima, isso significa que quando terminar em Z o próximo caractere é A. Distingui

Sua função deve ignorar caracteres especiais e os espaços.
'''
def criptCesar(word, cripto):
    cesar = ''
    for letter in word:
        if letter.isalpha():
            if ord(letter) + cripto > 90:
                cesar += chr(ord(letter) + cripto - 26)
            elif ord(letter) + cripto < 65:
                cesar += chr(ord(letter) + cripto + 26)
            else:
                cesar += chr(ord(letter)+cripto)
        else:
            cesar += letter
    
    return cesar