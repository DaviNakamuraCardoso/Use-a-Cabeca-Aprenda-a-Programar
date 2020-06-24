#definindo a abstração
def atribute(query, automatic):
    question = query + '[' + automatic + '] ?'
    answer = input(question)
    if answer == '':
        answer = automatic
    print('You chose:', answer)
    return answer

hair = atribute('What hair color', 'brown')
hair_lenght = atribute('What hair lenght', 'short')
eye = atribute('What eye color', 'blue')
gender = atribute('What gender', 'female')
glasses = atribute('Has glasses', 'no')
beard = atribute('Has beard', 'no')
