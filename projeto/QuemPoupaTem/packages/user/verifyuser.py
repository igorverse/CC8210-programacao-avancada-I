"""
It will verify if the typed cpf is already in the fake database.
Arguments:
    new_user_cpf: number of the cpf
Return:
    return a boolean value
"""


def verify_cpf(new_user_cpf):
    database = open('database.txt', 'r')

    for user in database:
        if str(new_user_cpf) in user:
            return False
    return True

"""
It will verify if the initial balance is right. Each account type has a special condition.
Arguments:
    account_type: a dic value representing the account type
Return:
    return a float value that represents the initial balance
"""

def verify_account_type(account_type):

    initial_balance = float(input('Saldo inicial: '))

    if account_type.lower() == 'conta salario':
        while (initial_balance < 0):
            print('\nInsira um saldo inicial maior ou igual a 0!')
            initial_balance = float(input('Saldo inicial: '))

    if account_type.lower() == 'conta corrente':
        while (initial_balance < -500):
            print('\nInsira um saldo inicial maior ou igual a -500!')
            initial_balance = float(input('Saldo inicial: '))

    if account_type.lower() == 'conta plus':
        while (initial_balance < -10000):
            print('\nInsira um saldo inicial maior ou igual a -10000')
            initial_balance = float(input('Saldo inicial: '))
    
    return initial_balance