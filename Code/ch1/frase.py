import random 

verbos = ['critica', 'mata', 'programa', 'odeia','fede']

complementos = ['bem', 'sempre', 'mal', 'muito']

sujeitos = [ 'Davi', 'Cauê', 'Suzana', 'Rogério', 'Gabrela']

verbo = random.choice(verbos)

complemento = random.choice(complementos)

sujeito = random.choice(sujeitos)

frase = sujeito + ' ' + verbo + ' ' + complemento

print(frase) 
