'''
Implemente uma função que receba um nome completo e apresente apenas o último nome e o 1o nome na seguinte forma:

último, 1o nome.
'''

def nomeCitacao(aName):
    name_array = aName.split(' ')
    author = name_array[len(name_array)-1] + ", " + name_array[0]
    
    return print(author)

print(nomeCitacao("Paulo Santos"))