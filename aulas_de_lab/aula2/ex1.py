'''
Neste exercício, você criará um programa que lê uma letra do alfabeto. 
Se o usuário digitar a, e, i, o ou u, seu programa deverá exibir uma mensagem 
indicando que a letra inserida é uma vogal. Se o usuário digitar y, seu programa 
deve exibir uma mensagem indicando que às vezes y é uma vogal 
(depende da língua, no inglês, por exemplo), e às vezes y é uma consoante. 
Caso contrário, seu programa deve exibir uma mensagem indicando que a letra é 
uma consoante. '''

letter = input('Digite a letra desejada: ')

vowel = letter == 'a' or letter =='e' or letter == 'i' or letter == 'o' or letter == 'u'

if (vowel):
    print ('Essa letra é uma vogal')

elif (letter == 'y'):
    print('Essa letra, em algumas línguas, pode ser considerada como uma vogal e, em outras, como uma consoante.')

else:
    print('Essa letra é uma consoante.')