'''
Um reservatório vazio deve ser abastecido por uma bomba. Conhecendo
se a vazão da bomba (em litros por segundo) e a capacidade do
reservatório (em litros). Calcule o tempo que levará para encher o
reservatório em: segundos, minutos e horas (quantidades inteiras).
'''

flowRate = float(input('Vazão da bomba em litros por segundo: '))
tankCapacity = float(input('Capacidade do reservatório em litros: '))

totalTime = tankCapacity / flowRate

hours = totalTime // 3600
minutes = ((totalTime / 3600 - hours) * 60) // 1
seconds = totalTime % 60

print('Tempo para encher o reservatório: %d segundos, %d minutos e %d horas' %(seconds, minutes, hours))