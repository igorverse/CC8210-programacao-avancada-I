def cleaner(filename):
    file = open(filename, 'r')
    cleanerFile = [file.readline().replace('width,height,', "")]

    for line in file:
        if 'ball' in line:
            cleanerFile.append(line)

    file.close()

    return cleanerFile

def removeColumns(filename):
    cleanerFile = []

    for line in cleaner(filename):
        cleanerFile.append(line.replace('640,360,', ""))

    return cleanerFile


if __name__ == '__main__':
    cleaner('annotations.csv')
    print(removeColumns('annotations.csv'))