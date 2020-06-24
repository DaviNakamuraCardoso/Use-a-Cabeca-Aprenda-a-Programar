import chomsky


def count_syllables_in_word(word):
    """
    This function counts the number of syllables in a word
    """
    count = 0

    endings = '!,;.?:'
    last_char = word[-1]

    if last_char in endings:
        processed_word = word[0:-1]
    else:
        processed_word = word

    if len(processed_word) <= 3:
        return 1
    if processed_word[-1] in 'Ee':
        processed_word = processed_word[0:-1]

    vowels = 'aeiouAEIOU'
    prev_char_was_vowel = False

    for char in processed_word:
        if char in vowels:
            if not prev_char_was_vowel:
                count += 1
            prev_char_was_vowel = True

        else:
            prev_char_was_vowel = False

    if processed_word[-1] in 'yY':
        count += 1

    return count


def count_syllables(words):
    """
    This function counts the syllables in the text's words
    """
    count = 0

    for word in words:
        word_count = count_syllables_in_word(word)
        count = count + word_count
    return count


def count_sentences(text):
    """
    This function counts the sentences in the text
    """
    count = 0
    terminals = '.;?!'
    for character in text:

        if character in terminals:
            count += 1

    return count



def compute_readability(text):
    """
    Based on the number of syllables, words and sentences, this function uses the formula developed by the US Marine to identify the readability of a text
    """
    total_words = 0
    total_sentences = 0
    total_syllables = 0
    score = 0

    words = text.split()
    total_words = len(text.split())
    total_sentences = count_sentences(text)
    total_syllables = count_syllables(words)

    score = 206.835 - 1.015 * ( total_words / total_sentences) - 84.6 * (total_syllables / total_words)
    if score > 90.00:
        answer = 'Texto de nível do 5º ano do Ensino Fundamental, facilmente compreendido por um aluno de 11 anos.'
    elif 90.00 >= score > 80.00:
        answer = 'Texto de nível do 6º ano do Ensino Fundamental, inglês coloquial para consumidores.'
    elif score <= 80.00 and score > 70.00:
        answer = 'Texto de nível do 7º ano do Ensino Fundamental, razoavelmente fácil de ler.'
    elif score <= 70.00 and score > 60.00:
        answer = 'Texto de nível do 9º ano do Ensino Fundamental, Inglês simples compreendido por adolescentes de 13 - 15 anos.'
    elif score <= 60.00 and score > 50.00:
        answer = 'Texto de 1º a 3º ano do Ensino Médio, razoavelmente difícil de ler.'
    elif score <= 50.00 and score > 30.00:
        answer = 'Texto de nível Universitário, difícil de ler.'
    else:
        answer = 'Texto de nível de Graduação, muito difícil de ler e mais bem-compreendido por universitários graduados.'

    print('Pontuação Total:', score, answer)






compute_readability(chomsky.text)
