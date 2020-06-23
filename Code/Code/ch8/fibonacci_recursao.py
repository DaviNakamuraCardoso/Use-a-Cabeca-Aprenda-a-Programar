import time

cache = {}


def fibonacci(n):
    try:
        n = int(n)
        global cache
        if n in cache:
            return cache[n]
        if n == 0:
            result = 0
        elif n == 1:
            result = 1

        else:
            result = fibonacci(n-1) + fibonacci(n-2)
            cache[n] = result
        return result
    except ValueError:
        return 'You crackudo man?'



numero = input('Numero')
print(fibonacci(numero))
