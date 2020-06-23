import sys

def make_crazy_libs(filename):
    try:
        file = open(filename, 'r')

        text = ''
        for line in file:
            text = text + process_line(line) + '\n'

        file.close()

        return text
    except FileNotFoundError:
        print('Não conseguimos encontrar o arquivo', filename, '.')
    except IsADirectoryError:
        print(filename, 'é um diretório.')
    except:
        print('Não consegui ler o arquivo', filename, '.')


placeholders = ['SUBSTANTIVO', 'VERBO_GERUNDIO', 'VERBO', 'ADJETIVO']


def process_line(line):
    global placeholders
    processed_line = ''

    words = line.split()
    for word in words:
        stripped = word.strip('.,;:?!')
        if stripped in placeholders:
            answer = input('Insira um ' + stripped + ':')
            processed_line = processed_line + answer
            if word[-1] in '.,:;?!':
                processed_line = processed_line + word[-1] + ' '
            else:
                processed_line = processed_line + ' '
        else:
            processed_line = processed_line + word + ' '

    return processed_line + '\n'


def save_crazy_lib(filename, text):
    try:
        file = open(filename, 'w')
        file.write(text)
        file.close()
    except:
        print('Desculpe, não foi possível escrever o documeneto')


def main():
    if len(sys.argv) != 2:
        print("crazy.py <filename>")
    else:
        filename = sys.argv[1]
        lib = make_crazy_libs(filename)
        if (lib != None):
            save_crazy_lib('crazy_' + filename, lib)


if __name__ == '__main__':
    main()

