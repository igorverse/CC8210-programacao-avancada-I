'''
Crie uma função chamada spellChecker() que recebe uma String e verifica se as palavras dessa String estão corretas, para verificação utilize o arquivo words.txt (o arquivo possui 466k palavras), que possuí todas as palavras do inglês. Sua função deverá retornar uma listas das palavras que não forem encontradas no arquivo.
'''

def spellChecker(words):
    myFile = open('words.txt', 'r')
    allLines = myFile.readlines()
    dic = []


    for a in '!?,.':
        words = words.replace(a, "")

    for w in allLines:
        dic.append(w.lower().rstrip('\n'))
        

    listOfWords = words.lower().split(' ')

    notFound = []

    for word in listOfWords:
        if word not in dic:
            notFound.append(word)


            

    return notFound

print(spellChecker("Hello World, Olá Mundo"))
print(spellChecker("Python is an interpreted, high-livel and geral-purpose programming languagem"))

