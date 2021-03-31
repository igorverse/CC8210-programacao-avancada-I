'''

Faça uma função chamada contaPalavras que receba uma String e que conte a quantidade de incidências de todas as palavras em uma String, assim listando todas as palavras e suas quantidades, considere como palavras as que tenha uma quantidade igual ou maior que duas letras.
A função deverá retornar duas listas, uma referente as palavras encontradas (sem duplicidade), e outra lista referente a quantidade de incidência de cada uma das palavras respectivamente a lista de palavras.
Sua função deverá considerar todas as palavras como letras minusculas, remova também as virgulas e os caracteres "!" e "?".

'''


def contaPalavras(words):
    for a in '!?,':
        words = words.replace(a, "")

    word_array = words.lower().split(" ")
    filtered_word_array = []
    no_repeat_words = []

    counter = []

    for word in word_array:
        if len(word) >= 2:
            filtered_word_array.append(word)

    for word in filtered_word_array:
        if word not in no_repeat_words:
            counter.append(word_array.count(word))
            no_repeat_words.append(word)

    return no_repeat_words, counter

p = " e fei a Fei feijão FeI Feijão felino Feio i Fé"
print(contaPalavras(p))