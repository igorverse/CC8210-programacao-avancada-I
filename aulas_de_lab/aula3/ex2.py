'''
Crie um programa que leia números inteiros do usuário até que o número 0 seja inserido.
Uma vez que todos os números inteiros tenham sido lidos, seu programa deve exibir todos os números negativos, seguidos por todos os números positivos.
Dentro de cada grupo, os números devem ser exibidos na mesma ordem em que foram inseridos pelo usuário

'''
positive_numbers = []
negative_numbers = []

while True:
    number = int(input())
    if number == 0:
        break
    else:
        if number > 0:
            positive_numbers.append(number)
        else:
            negative_numbers.append(number)

print(str(negative_numbers)[1:-1])
print(str(positive_numbers)[1:-1])