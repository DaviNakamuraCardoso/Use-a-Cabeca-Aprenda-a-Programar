altura = input('Qual é a sua altura? ')

massa = input('Qual é sua massa? ')

imc = int(massa) / float(altura) ** 2
while imc <= 30 and imc >= 18.5:
    print('Seu Índice de Massa Corporal é ', imc, '.', 'O valor normal é de 18,50 a 24,99.' )
    input(massa)
    input(altura)
else:
    print('Seu IMC está fora do valor normal')
    
   
