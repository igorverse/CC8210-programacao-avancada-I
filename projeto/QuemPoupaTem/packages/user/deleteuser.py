"""
It can be used to delete the user from the fake database.
Arguments:
    function without arguments.
Return:
    void
"""


from json import loads

def delete_user():
    print('\nAo digitar o CPF, a conta será apagada!\n')
    cpf = input('Digite seu cpf: ')
    new_lines = []

    database = open('database.txt', 'r')

    for line in database.readlines():
        if cpf not in loads(line).values():
            new_lines.append(line)
        else:
            print('\nConta fechada com sucesso.')

    database = open('database.txt', 'w')

    formated_database = []

    for i in range(len(new_lines)):
        if new_lines[i] == new_lines[len(new_lines)-1]:
            formated_database.append(new_lines[i].rstrip('\n'))
        else:
            formated_database.append(new_lines[i])
    
    database.writelines(formated_database)

    database.close()