'''
Crie uma Lista de números inteiros V[5]. Inicialize esse
vetor com números fixos e aleatórios (a sua escolha).
Exiba como saída a média dos valores desse vetor.
OBRIGATÓRIO O USO DE LAÇO DE REPETIÇÃO PARA LEITURA DA LISTA.

'''

lista = []

for x in range(5):
    valor = int(input('insira um número inteiro: '))
    lista.append(valor)

soma = 0
for x in lista:
    soma += x

media = soma/len(lista)

print("A média é %.2f" %media)