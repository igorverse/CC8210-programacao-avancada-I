'''
Newton descobriu um método para aproximar os valores das raízes de uma equação numérica. Esse método é bastante simples e é conhecido como método de Newton. Escreva um programa que implemente o método de Newton para calcular e exibir a raiz quadrada de um número x digitado pelo usuário. O algoritmo (pseudocódigo) para o método de Newton é o seguinte:
'''

x = int(input('Digite o número desejado: '))
guess = x / 2
miss = abs(guess ** 2 - x)

while miss > 10 ** (-12):
    guess = (guess + x / guess) / 2
    miss = guess ** 2 - x

print('%.3f' %guess)


