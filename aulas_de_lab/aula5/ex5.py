'''
Escreva uma função com parâmetros chamada multiplo(x, y). 
Esta função deve receber dois números e retornar True se o primeiro for múltiplo do segundo número; a função retorna False caso contrário.
'''

def multiplo(x, y):
    if (x % y == 0):
        return True
    else:
        return False

print(multiplo(5, 10))
print(multiplo(50, 10))