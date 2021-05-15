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
