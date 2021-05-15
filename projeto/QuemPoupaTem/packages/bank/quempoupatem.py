"""
It will allow to realize the avaliable operations of the Quem Poupa Tem bank.
Arguments:
    function without arguments
Return:
    void function
"""

import os
from ..menu import menu
from ..user.createuser import new_bank_custommer
from ..user.deleteuser import delete_user
from ..banking.withdraw import withdraw
from ..banking.deposit import deposit
from ..banking.showbalance import show_balance
from ..banking.bankstatement import bank_stateament


def quem_poupa_tem():
    if not(os.path.isfile('database.txt')):
        database = open('database.txt', 'w')

    print('\n----> Seja bem-vindo ao banco Quem Poupa Tem! Selecione uma operação: <----\n')

    while True:
        menu_option = menu()
        if menu_option == 1:
            new_bank_custommer()
        elif menu_option == 2:
            delete_user()
        elif menu_option == 3:
            withdraw()
        elif menu_option == 4:
            deposit()
        elif menu_option == 5:
            show_balance()
        elif menu_option == 6:
            bank_stateament()
        elif menu_option == 0:
            print('\nSAINDO DO BANCO!')
            break
        else:
            print('\nOPERAÇÃO INVÁLIDA!')