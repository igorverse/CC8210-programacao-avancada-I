"""
It will show the bank statement of the custommer
Arguments:
    function without arguments
Return:
    void function
"""


from json import loads

def bank_stateament():
    cpf = input('cpf: ')
    password = input('senha: ')

    database = open('database.txt', 'r')

    database_as_a_list = []
    
    for line in database.readlines():
        database_as_a_list.append(loads(line))

    valid_informations = False
    
    for line in database_as_a_list:

        if (cpf == line["cpf"] and password == line["password"]):
            print('\n=========== Extrato bancário ==========\nNome: %s\nCPF: %s\n%s' %(line["name"], line["cpf"], line["account type"]))
            for item in line["banking date"]:
                print("Data:    ", item)
            valid_informations = True

    if (valid_informations == False):
        print('\nDADOS INVÁLIDOS')