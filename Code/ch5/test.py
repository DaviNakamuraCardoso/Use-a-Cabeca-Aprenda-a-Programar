
def allow_access(code):
    if code == 1914:
        answer = True
        return answer
    else:
        answer = False
        return answer

code = int(input('Qual é a senha? '))
answer = allow_access(code)
phrase = 'F22raptor'
if answer == True:
    print(phrase)
else:
    print('Get away')
saida = input('Encerrar programa? ')
if saida == 'sim':
    print('Até logo!')
else:
    i = 0
    for i in range(0,9):
      saida = input('Não quer sair? ')
      i += 1
    

    
        
        
        
    
    
    
    
    
