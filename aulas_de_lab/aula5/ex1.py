'''
Implemente uma função chamada analise que recebe uma lista e retorne a media, mediana, o valor mínimo e o máximo respectivamente, independente do tamanho da lista.
'''

def analise(numbers):
    numbers = sorted(numbers)

    mean = sum(numbers)/len(numbers)
    median = 0

    if (len(numbers) % 2 == 0):
        median = (numbers[int((len(numbers)-1)/2 + 0.5)] + numbers[int((len(numbers)-1)/2 -0.5)]) / 2
    else:
        median = numbers[int((len(numbers)/2))]

    minValue = numbers[0]
    maxValue = numbers[0]
    for n in numbers:
        if n < minValue:
            minValue = n
        if n > maxValue:
            maxValue = n

    return mean, median, minValue, maxValue

print(analise([2, 5, 7, -2, 8]))
    

