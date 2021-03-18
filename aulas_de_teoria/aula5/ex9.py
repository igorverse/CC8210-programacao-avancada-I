'''
Escreva uma função que receba duas listas de números inteiros e
retorne uma lista seja a intersecção dessas duas listas.
Obs.: Intersecção é quando um valor estiver nas duas lista. Garanta
que não haja elementos duplicados em cada uma dessas duas listas
(use a função do exercício 06 para eliminar os valores duplicados). 
'''

def intersection(list1, list2):
    list1 = list(set(list1))
    list2 = list(set(list2))
    final_list = []
    for n in list1:
        if n in list2:
            final_list.append(n)

    return final_list

print(intersection([1,2,3,4,5,6,4], [4,5,6,7,8,9,10]))
