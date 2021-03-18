'''
Exercício 04

a) Escreva uma função que receba quatro parametros referente a notas de
atividades do aluno e retorne a media dessa 4 notas, caso algumas notas
não sejam atribuidas na chamada da função, atribuir como padrão o valor
zero para essa notas.

b) Escreva uma função lambda que receba quatro parametros referente a
notas de atividades do aluno e retorne a media dessa 4 notas, caso
algumas notas não sejam atribuidas na chamada da função, atribuir como
padrão o valor zero para essa notas.

'''

# A)

def gradeAverage(grade1 = 0, grade2 = 0, grade3 = 0, grade4 = 0):
    return (grade1 + grade2 + grade3 + grade4) / 4

print(gradeAverage(10, 10, 10, 10))
print(gradeAverage(10, 10, 10))
print(gradeAverage(grade4 = 4))

# B)

studentAverage = lambda grade1 = 0, grade2 = 0, grade3 = 0, grade4 = 0: (grade1 + grade2 + grade3 + grade4) / 4

print(studentAverage(10, 10, 10, 10))
print(studentAverage(10, 10, 10))
print(studentAverage(grade4 = 4))