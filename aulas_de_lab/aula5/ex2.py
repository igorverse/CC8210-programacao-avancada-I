'''
Escreva uma função com parâmetros que retorne o maior de dois números. A função deve se chamar maximo(x, y), esse função também deverá ter mais um parâmetro opcional chamado imprime, que por padrão é Falso, mas quando True, deverá imprimir o valor máximo.
'''

def maximo(x, y, imprime = False):
    ref = x
    if y > ref:
        ref = y
    
    if imprime == True:
        print(ref)

    return ref
