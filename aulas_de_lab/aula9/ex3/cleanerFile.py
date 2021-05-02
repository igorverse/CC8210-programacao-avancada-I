from fileCleaner import cleaner, removeColumns

def main(filename):
    newFile = open('cleanerAnnotations.csv', 'w')

    cleaner(filename)

    for line in removeColumns(filename):
        newFile.write(line)

    newFile.close()


if __name__ == '__main__':
    main('annotations.csv')


