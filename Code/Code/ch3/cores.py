#comandos iniciais
import random

#escolhendo uma cor
escolha_do_computador = random.randint(0,5)
if escolha_do_computador == 0:
    cor = 'vermelho'
elif escolha_do_computador == 1:
    cor = 'laranja'
elif escolha_do_computador == 2:
    cor = 'amarelo'
elif escolha_do_computador == 3:
    cor = 'verde'
elif escolha_do_computador == 4:
    cor = 'azul'
else:
    cor = 'roxo'

tentativa = input('Tente adivinhar em qual cor estou pensando. (Vermelho, laranja, amarelo, verde, azul ou roxo) ')
número_de_tentativas = 1

while tentativa != cor:
    print('Errou!')
    número_de_tentativas = int(número_de_tentativas) + 1
    tentativa = input('Tente novamente! ')
print('Acertou! Eu estava pensando em', cor,'. Número de tentativas: ', número_de_tentativas)
