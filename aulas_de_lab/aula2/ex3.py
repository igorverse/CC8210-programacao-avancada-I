'''

Um funcionário de uma empresa recebe aumento salarial anualmente. Sabe-se que: 

a) Esse funcionário foi contratado em 2005, com salário inicial de R$ 5.000,00; 

b) Em 2006 ele recebeu aumento de 1,5% sobre o salário inicial; 

c) A partir de 2007 (inclusive), os aumentos salariais sempre corresponderam ao dobro do percentual do ano anterior. 

Faça um programa que recebe um ano (ano > 2007) e determina o salário atual do funcionário.

'''

tax = 0.015
salary = 5000 + (5000 * tax)
year = int(input('Digite o ano desejado: '))
countYear = year

while year <= 2007:
    year = int(input('Digite o ano desejado: '))

while countYear > 2006:
    tax += tax
    salary += salary * tax
    countYear -= 1


print('Salário de %s: R$ %.2f' %(year, salary))