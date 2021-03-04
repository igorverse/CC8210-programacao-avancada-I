'''
Crie uma Lista de números inteiros de tamanho 5.
Preencha essa Lista com entradas fornecidas pelo usuário.
Exiba como saída o conteúdo do índice 3 dessa Lista.
(Usar estrutura de repetição)
'''

# Usando while:

lista = []

counter = 0 
while counter < 5:
    lista.append(int(input('insira um número inteiro: ')))
    counter += 1

print(lista[3])

# Usando for: 

lista2 = []
for x in range(5):
    valor = int(input('insira um número inteiro: '))
    lista2.append(valor)

print(lista2[3])