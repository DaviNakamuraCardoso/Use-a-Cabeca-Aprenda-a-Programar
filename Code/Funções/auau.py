def latido (nome, peso):
    if peso > 20:
        print (nome, 'diz WOOF WOOF')
    else:
        print(nome, 'diz woof woof')

latido('Codie', 40)
latido('Jackson', 12 )
latido('Fido', 50 )
latido('Sparky', 9 )
nome = input('Qual é o nome do seu cachorro? ')
peso = input('Qual é o peso do seu cachorro? ')
latido(nome, int(peso))
