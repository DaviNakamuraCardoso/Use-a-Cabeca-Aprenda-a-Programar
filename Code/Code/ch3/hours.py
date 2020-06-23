import sys


def month_hours(filename, today):
    file = open(filename, 'r')
    for hours in file:
        hours = float(hours)
        hours = hours + today
        file = open(filename, 'w')
        hours = str(hours)
        file.write(hours)
        print('Você fez', hours, 'este mês.')
        if float(hours) >= 30.0:
            print('Parabéns, você atingiu a meta de 30 horas!')


if len(sys.argv) != 2:
    print('Arquivos insuficientes')
else:
    filename = sys.argv[1]
    horas = float(input('Quantas horas de campo você fez hoje? '))
    month_hours(filename, horas)





