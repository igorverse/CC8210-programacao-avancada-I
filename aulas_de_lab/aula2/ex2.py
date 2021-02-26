'''
Posições em um tabuleiro de xadrez são identificadas por uma letra e um número. 
As letras identificam as colunas, enquanto os números identificam as linhas, 
conforme mostrado abaixo:

...

Escreva um programa que leia uma posição inserida por um usuário. 
Primeiro a coluna, depois a linha. Então, seu programa deve informar qual é a 
cor do quadrado relacionado à posição digitada.

Para isso, use uma declaração if para determinar se a coluna começa com um 
quadrado preto ou um quadrado branco. Em seguida, use modular aritmética (%) para 
relatar a cor do quadrado nessa linha. Por exemplo, se o usuário entrar a - 1 
então seu programa deve informar que o quadrado é preto. Se o usuário digitar d - 5
então seu programa deve informar que o quadrado é branco. Seu programa pode 
assumir que uma posição válida sempre será inserida.

'''

line = int(input('Digite a linha desejada: '))
column = input('Digite a coluna desejada: ')

black = column == 'a' or column == 'c' or column == 'e' or column == 'g'
white = column == 'b' or column == 'd' or column == 'f' or column == 'h'

sumColor = 0

if (black):
    sumColor += 1
else:
    sumColor = 0

if (line % 2 == 0):
    sumColor += 1

if(sumColor % 2 == 0):
    print ('Branco')
else:
    print('Preto')