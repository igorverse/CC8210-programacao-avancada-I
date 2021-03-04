'''

Faça um algoritmos que armazene 10 números inteiros
informados pelo usuário em uma Lista. Exiba como saída
o MAIOR numero dessa Lista.
OBRIGATÓRIO O USO DE LAÇO DE REPETIÇÃO PARA LEITURA DA LISTA.

'''

lista = []
for x in range(10):
    valor = int(input('insira um número inteiro: '))
    lista.append(valor)

print(lista)

maior = lista[0]
for x in lista:
    if x > maior:
        maior = x

print(maior)