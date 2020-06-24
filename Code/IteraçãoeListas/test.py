personagens = ['Batman', 'Mulher gato', 'Bane', 'Duas-caras']
identidades = ['Bruce Wayne', 'Selina Kyle', 'Bane Dorrance', 'Harvey Dent']


for personagem, identidade in zip(personagens, identidades):
    print('O nome de', personagem, 'é', identidade)
