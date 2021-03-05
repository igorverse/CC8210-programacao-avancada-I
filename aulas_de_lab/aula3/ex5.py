'''

Crie um programa que leia números inteiros de uma lista de temperatura de um sensor. 

Esse sensor está com falha na comunicação, e aleatoriamente ele apresenta valores incorretos (outliers), neste contexto são considerados valores incorretos números acima de 100 e menores que -10. Remova da lista todos os valores considerados incorretos e exiba em formato de lista os valores corretos de temperatura.

Atenção: Os valores da lista temperaturas são fornecidos pelo programa do Moodle, faça o código sem declarar a lista, apenas use a lista fornecida.

'''

temperatures = [-4, -2, 10, 5, 11, 204, -17, 12, 20, 22, -58, 21, 19, 17, 999] #Enviado sem essa linha.
correct_temperatures = []

for i in range(len(temperatures)):
    if temperatures[i] <= 100 and temperatures[i] >= -10:
        correct_temperatures.append(temperatures[i])

print(temperatures)
print(correct_temperatures)
print('Média igual a %.1f' %(sum(correct_temperatures)/len(correct_temperatures)))