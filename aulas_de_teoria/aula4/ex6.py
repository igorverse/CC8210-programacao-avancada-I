'''
Escreva um programa que lê do teclado uma matriz de
números reais com quatro linhas e três colunas e imprime na
tela a matriz. Depois lê um valor digitado pelo usuário e
procura este valor na matriz. Se encontrar o valor, mostra
sua posição (ou índice). Se não encontrar este valor no vetor,
mostra na tela uma mensagem que não achou.
'''

matrix = []

for i in range(4):
    i = []
    for _ in range(3):
        i.append(float(input()))
    matrix.append(i)

user_guess = float(input('guess: '))

ai = 0
aj = 0
counter = 0

print('')
print(matrix)

for line in matrix:
    ai += 1
    for a in line:
        aj += 1
        if a == user_guess:
            counter += 1
            print()
            print('index: i = %d e j = %d' %(ai, aj))
    aj = 0

if counter < 1:
    print('valor não encontrado.')
