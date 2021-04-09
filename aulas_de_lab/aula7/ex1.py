'''
Crie uma função chamada verifica() que receba o nome de um arquivo e verifica se o arquivo existe. Retorne true se existir, e false se não existir.
'''

import os

def verifica(filename):
    
    return os.path.isfile(filename)
