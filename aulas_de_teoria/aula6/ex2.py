'''

Faça um algoritmo que conte a quantidade de incidências de todas as palavras
em uma String , assim listando todas as palavras e suas quantidades, considere
como palavras as que tenha uma quantidade igual ou maior que duas letras.

'''

words = input("Digite uma palavra: ").lower()

word_array = words.split(" ")

showed_word = []

for word in word_array:
    if len(word) < 2:
        word_array.remove(word)

for word in word_array:
    if word not in showed_word:
        print("a palavra %s aparece %i vezes." %(word, word_array.count(word)))
    showed_word.append(word)