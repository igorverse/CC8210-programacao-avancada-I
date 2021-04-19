'''
Crie uma função em Python chamada contaPalavras que recebe uma string e que conte a quantidade de incidências de todas as palavras em uma string, assim listando todas as palavras e suas quantidades. Sua função deve  retornar o número de palavras contadas  em formato de dicionário.

A função deverá retornar um dicionário referente as palavras encontradas (sem duplicidade) e a quantidade de incidência de cada uma das palavras.

Sua função deverá considerar todas as palavras como letras minúsculas, remova também as virgulas e os caracteres "!" e "?".

Obs: Utilize dicionário para solucionar o problema, conforme apresentado em aula.
'''

def contaPalavras(words):
    for a in '!?,.':
        words = words.replace(a, "")

    listOfWords = words.lower().split(' ')

    dic = {}

    for word in listOfWords:
        if len(word) > 0:
            if word in dic.keys():
                dic[word] += 1
            else:
                dic[word] = 1

    return dic

p = " vou testar com testes, um teste, muitos testes, sempre Testando com Testes, muitos testes, mais testes, testes!!!"

print(contaPalavras(p))