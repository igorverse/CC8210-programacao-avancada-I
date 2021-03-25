'''

Peça ao usuário uma string e imprima se essa string é um palíndromo ou não.
o
Palíndromo é uma palavra ou frase (normalmente, ignorando se os espaços em branco) que se
pode ler, indiferentemente, da esquerda para a direita ou vice versa.
o
Exemplos: “ovo”; “a grama é amarga”; “A sacada da casa”, “Luz azul”.

'''


word = input('Digite uma palavra: ').replace(" ", "").lower()

if word == word[::-1]:
    print('essa string é um palíndromo'.capitalize())

else:
    print('essa string não é um palíndromo'.capitalize())