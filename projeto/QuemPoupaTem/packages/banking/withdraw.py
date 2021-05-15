"""
It will register a withdraw of the user in the fake database.
Arguments:
    function without arguments
Return:
    void function
"""


from json import loads, dumps
from .bankingdate import banking_date


def withdraw():
    cpf = input('cpf: ')
    password = input('senha: ')

    database = open('database.txt', 'r')

    database_as_a_list = []
    
    for line in database.readlines():
        database_as_a_list.append(loads(line))

    valid_informations = False
    
    for line in database_as_a_list:

        if (cpf == line["cpf"] and password == line["password"]):
            if line["account type"].lower() == "conta salario":
                new_withdraw = float(input('Valor do saque: '))
                tax = new_withdraw * 0.02
                new_balance = line["balance"] - (tax + new_withdraw)
                if (0 > new_balance):
                    print('\nSAQUE NÃO PERMITIDO! SALDO INSUFICIENTE!')
                else:
                    line["balance"] = new_balance
                    line["banking date"].append(banking_date() + "  -" + "  " + str(new_withdraw) + "  Tarifa:  " + str(tax) + "   Saldo: %s" %line["balance"])
                    print('\nSAQUE REALIZADO!')
            elif line["account type"].lower() == "conta corrente":
                if line["account type"].lower() == "conta corrente":
                    new_withdraw = float(input('Valor do saque: '))
                    tax = 0.03 * new_withdraw
                    new_balance = line["balance"] - (tax + new_withdraw)
                    if (-500 > new_balance):
                        print('\nSAQUE NÃO PERMITIDO! SALDO INSUFICIENTE!')
                    else:
                        line["balance"] = new_balance
                        line["banking date"].append(banking_date() + "  -" + "  " + str(new_withdraw) + "  Tarifa:  " + str(tax) + "   Saldo: %s" %line["balance"])
                        print('\nSAQUE REALIZADO!')
            else:
                if line["account type"].lower() == "conta plus":
                    new_withdraw = float(input('Valor do saque: '))
                    tax = new_withdraw * 0.01
                    new_balance = line["balance"] - (tax + new_withdraw)
                    if (-10000 > new_balance):
                        print('\nSAQUE NÃO PERMITIDO! SALDO INSUFICIENTE!')
                    else:
                        line["balance"] = new_balance
                        line["banking date"].append(banking_date() + "  -" + "  " + str(new_withdraw) + "  Tarifa:  " + str(tax) + "   Saldo: %s" %line["balance"])
                        print('\nSAQUE REALIZADO!')

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
    
    if (valid_informations == False):
        print('\nDADOS INVÁLIDOS')