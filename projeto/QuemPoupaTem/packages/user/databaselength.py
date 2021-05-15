"""
It gets the lenght of a generic fake database.
Arguments:
    filename: a string with the name of the file
Return:
    it returns the lenght of the generic database.
"""

def database_length(filename):

    database = open(filename, 'r')

    len_of_database = len(database.readlines())

    database.close()

    return len_of_database