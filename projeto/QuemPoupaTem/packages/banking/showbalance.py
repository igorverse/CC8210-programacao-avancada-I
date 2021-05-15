"""
It will show the balance of the custommer
Arguments:
    function without arguments
Return:
    void function
"""


from json import loads

def show_balance():
    cpf = input('cpf: ')
    password = input('senha: ')

    database = open('database.txt', 'r')

    database_as_a_list = []
    
    for line in database.readlines():
        database_as_a_list.append(loads(line))

    valid_informations = False
    
    for line in database_as_a_list:

        if (cpf == line["cpf"] and password == line["password"]):
            print('\nSaldo atual: ' + str(line["balance"]))
            valid_informations = True

    if (valid_informations == False):
        print('\nDADOS INVÁLIDOS')