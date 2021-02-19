'''
Faça um programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês e calcule e mostre o total do
seu salário no referido mês, sabendo se que são descontados 11%
para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
faça um programa que nos dê:

- salário bruto.
- Quanto pagou ao INSS.
- Quanto pagou ao sindicato.
- salário líquido.
'''

moneyPerHour = float(input('Salário por hora: '))
hoursWorked = float(input('Horas trabalhadas no mês: '))
grossSalary = moneyPerHour * hoursWorked
taxesINSS = grossSalary * 0.08
sindicateTaxes = grossSalary * 0.05
netSalary = grossSalary - (grossSalary * 0.24)

print('Salário bruto: %.2f \n Pago ao INSS: %.2f \n Pago ao sindicato: %.2f \n Salário líquido: %.2f' %(grossSalary, taxesINSS, sindicateTaxes, netSalary))