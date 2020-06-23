palavras = ['asa', 'taco', 'tacocat', 'arara', 'gato', 'caue', 'radar']


def palindromos(lista):
    for palavra in lista:
        classificacao = None
        for i in range(len(palavra)):
            if palavra[i] == palavra[-i-1]:
                classificacao = 'é palindromo'
            else:
                classificacao = 'não é palindromo'

        print(palavra, classificacao)


palindromos(palavras)
