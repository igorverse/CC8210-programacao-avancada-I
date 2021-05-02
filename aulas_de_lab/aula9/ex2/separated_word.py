

def sortedWords(words):

    return (','.join((sorted(words.split('-'))))).replace(',', '-')


def caseCounter(words):
    lowerCase = 0
    upperCase = 0

    words = words.replace('-','')

    for letter in words:
        if letter == letter.lower():
            lowerCase += 1

        if letter == letter.upper():
            upperCase += 1

    return ('Maísculas: %i \n\nMinúsculas: %i' %(upperCase, lowerCase))



if __name__ == '__main__':
    print(sortedWords('Python-Dados-OpenCV-Java-DataScience'))
    print(caseCounter('Python-Dados-OpenCV-Java-DataScience'))