fibonaccis = {1: 1, 2: 1, 3: 2}


def get_fibonacci(q):
    for q in range(4, 100001):
        fibonaccis[q] = fibonaccis[q-1] + fibonaccis[q-2]


def fibonacci_det(q):
    try:
        global fibonaccis
        q = int(q)
        if q in fibonaccis:
            return fibonaccis[q]
        else:
            fibonaccis[(q - 1)] = 'inexistente'

        print('O', str(q) + 'º número na sequência de Fibonacci é', fibonaccis[(q - 1)])
    except ValueError:
        print('You crackudo man?')

get_fibonacci(1000000)
user_comand = ''
while user_comand != 'sim':
    number = input('Posição do número desejado: ')
    print(fibonacci_det(number))
    user_comand = input('Encerrar programa? ')

