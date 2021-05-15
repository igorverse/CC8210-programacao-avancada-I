"""
It will register a deposit of the user in the fake database.
Arguments:
    function without arguments
Return:
    void function
"""


from json import loads, dumps
from .bankingdate import banking_date


def deposit():
    cpf = input('cpf: ')

    database = open('database.txt', 'r')

    database_as_a_list = []
    
    for line in database.readlines():
        database_as_a_list.append(loads(line))


    valid_informations = False

    for line in database_as_a_list:

        if (cpf == line["cpf"]):
            new_deposit = float(input('Valor do deposito: '))
            line["balance"] += new_deposit

            line["banking date"].append(banking_date() + "  +" + "  " + str(new_deposit) + "  Tarifa: 0.00" + "   Saldo: %s" %line["balance"])

            formated_database = []

            for i in range(len(database_as_a_list)):
                if database_as_a_list[i] == database_as_a_list[len(database_as_a_list)-1]:
                    formated_database.append(dumps(database_as_a_list[i]))
                else:
                    formated_database.append(dumps(database_as_a_list[i]) + '\n')

            database = open('database.txt', 'w')
            database.writelines(formated_database)
            database.close()

            valid_informations = True

            print('\nDEPÓSITO EFETUADO!')
            
    if (valid_informations == False):
        print('\nDADOS INVÁLIDOS')