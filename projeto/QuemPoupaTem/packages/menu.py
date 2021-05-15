"""
It shows a menu with the bank operations.
Arguments:
    function without arguments.
Return:
    return a int with the selected option.
"""

def menu():
    print('\n1 - Novo Cliente\n2 - Apaga Cliente\n3 - Debita\n4 - Deposita\n5 - Saldo\n6 - Extrato\n\n\n0 - Sai\n')
    number_selected = int(input('Digite o número da operação: '))

    return number_selected