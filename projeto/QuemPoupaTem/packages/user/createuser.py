"""
It creates a new custommer of the bank and save him in a "fake" database.
Arguments:
    function without arguments.
Return:
    return a list with the solicited values (name, cpf, bank account type, initial balance, user password and banking operations date).
"""
from .verifyuser import verify_cpf, verify_account_type
from .accounttype import account_type
from json import dumps
from .databaselength import database_length

def new_bank_custommer():

    name = input("Nome: ")

    validate_cpf = 0
    while validate_cpf != 11:
        cpf = input("Digite o seu CPF (apenas números): ")
        validate_cpf = len(cpf)
        if len(cpf) != 11:
            print('Atenção! CPF deve ter 11 dígitos!\n')

    custommer_account_type = account_type()

    new_custommer = {
        "name": name,
        "cpf": cpf,
        "account type": custommer_account_type,
        "balance": verify_account_type(custommer_account_type),
        "password": (input("Cadastre uma senha: ")),
        "banking date": []
    }

    if not(verify_cpf(new_custommer["cpf"])):
        print('\nEste CPF já foi cadastrado. CONTA NÃO SERÁ CADASTRADA!')
    else:
        print('\nCONTA CADASTRADA COM SUCESSO!')

        database = open('database.txt', 'r+')
        database.read()
        
        if (database_length('database.txt') == 0):
            database.writelines(dumps(new_custommer))
        else:
            database.writelines('\n' + dumps(new_custommer))

        database.close()

    return new_custommer