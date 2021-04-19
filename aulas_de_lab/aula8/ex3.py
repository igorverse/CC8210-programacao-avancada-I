'''

Um dicionário pode ser utilizado para representar um estoque de uma empresa. Nele, todos os itens de uma empresa são registrados, anotando a quantidade de itens disponíveis e o seu valor unitário.

Faça um programa que permita gerenciar um estoque de uma Quitanda. O programa deve permitir inserir itens no estoque, remover itens, modificar a quantidade e preço de um item e imprimir todo o estoque. 

Faça este programa usando funções e dicionários.

Teste o programa criando e manipulando um estoque de frutas.

Exemplo Dicionário:

dicionario = {'maça': {'Quantidade': 100, 'Preco': 1.5} , 'banana': {'Quantidade': 12, 'Preco': 3.2} }

'''

quintanda = {}

def insert(item):
    quantity = int(input('Quantidade: '))
    price = float(input("Preco: "))

    infos = {
        "Quantidade": quantity,
        "Preco": price
    }

    quintanda[item] = infos

    return (item.upper() + ' adicionado à quintanda.\n')

def remove(item):
    if item in quintanda.keys():
        confirmation = input('Tem certeza que deseja remover %s? (Digite SIM ou NAO): ' %item.upper()).lower()

        for w in 'ã':
            confirmation = confirmation.replace(w, "a")

        while True:
            for w in 'ã':
                confirmation = confirmation.replace(w, "a")

            if confirmation == 'sim' or confirmation == 'nao':
                break
            else:
                print('\n Opção inválida. Digite novamente \n')
                confirmation = input('Tem certeza que deseja remover %s? (Digite SIM ou NAO): ' %item.upper()).lower()


        if confirmation == 'sim':
            del quintanda[item]
            return ('Remoção efetuada.\n')
        else:
            return ('Remoção cancelada.\n')


    return (item.upper() + ' não está presente na quintada.')

def modify(item):
    if item in quintanda.keys():
        print('\n %s será modificado. \n' %item.upper())
        insert(item)

        return 'Quantidade e/ou preço atualizado(s).'

    return (item.upper() + ' não está presente na quintada.')

def printAll(items):
    print(items)





# TESTES

print(insert('maça'))
print(insert('tomate'))

print(remove('maça'))

print(insert('abacaxi'))


printAll(quintanda)

print(modify('tomate'))

printAll(quintanda)