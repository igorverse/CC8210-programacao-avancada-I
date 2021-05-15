"""
It determines the account type.
Arguments:
    function without arguments.
Return:
    return a string with the name of the account type.
"""


def account_type():
        while True:
            user_account_type = int(input('\n1 - conta salário\n2 - conta corrente\n3 - conta plus\n\nSelecione o tipo de conta: '))
            if (user_account_type == 1 or user_account_type == 2 or user_account_type == 3):
                break
            else:    
                print('\nInsira um valor inteiro válido. Opções possíveis: 1, 2 ou 3.')


        choosen_type = user_account_type

        if choosen_type == 1:
            return 'Conta Salario'

        if choosen_type == 2:
            return 'Conta Corrente'

        if choosen_type == 3:
            return 'Conta Plus'
