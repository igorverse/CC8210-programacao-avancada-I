'''
Newton descobriu um método para aproximar os valores das raízes de uma equação
numérica. Esse método é bastante simples e é conhecido como método de Newton.
Escreva uma função que implemente o método de Newton para calcular e exibir a raiz
quadrada de um número x digitado pelo usuário.
O algoritmo (pseudocódigo) para o método de Newton é o seguinte: 

Receba x
Inicialize a variável palpite para ser igual a x/2
Inicialize a variável erro para ser igual a |palpite2 - x |
Enquanto erro > 10^-12 faça
    Atualize palpite para ser igual a média entre palpite e x/palpite
    Atualize erro para ser igual a diferença entre palpite2 e x
Retorne palpite 

'''

def root_square(x):
    guess = x/2
    miss = abs(guess ** 2 - x)
    while miss > 10 ** (- 12):
        guess = (guess + x/guess) / 2
        miss = (guess ** 2) - x
    return guess


print(root_square(25))
print(root_square(49))
print(root_square(144))
print(root_square(42))