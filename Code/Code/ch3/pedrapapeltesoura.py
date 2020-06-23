#definições iniciais

import random

winner = ''

#definindo a escolha do computador
random_choice = random.randint(0,2)

if random_choice == 0:
    computer_choice = 'pedra'
elif random_choice == 1:
    computer_choice = 'papel'
else:
    computer_choice = 'tesoura'

#input com a escolha do usuario
user_choice = ''
while (user_choice != 'pedra' and
       user_choice != 'papel' and
       user_choice != 'tesoura'):
    user_choice = input('Pedra, papel ou tesoura? ')
    
#definição do vencedor 
if computer_choice == user_choice:
    winner = 'Empate'
elif computer_choice == 'pedra' and user_choice == 'tesoura': 
    winner = 'Computador'
elif computer_choice == 'papel' and user_choice == 'pedra':
    winner = 'Computador'
else: 
    winner = 'Jogador'

#mensagem final

if winner == 'Empate': 
    print('Nós dois escolhemos', computer_choice, 'jogue novamente')
else:
    print('O', winner, 'venceu. O computador escolheu', computer_choice, '.')
    
