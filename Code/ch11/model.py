import random

altura = int(100)
largura = int(100)


def randomizar(grade, largura, altura):
    for i in range (0, largura):
        for j in range(0, altura):
            grade[i][j] = random.randint(0, 1)


modelo_de_grade = [0] * altura
proxima_grade = [0] * altura
for i in range(0, altura):
    modelo_de_grade[i] = [0] * largura
    proxima_grade[i] = [0] * largura


def next_gen():
    global modelo_de_grade, proxima_grade

    for i in range(0, altura):
        for j in range(0, largura):
            cell = 0
            count = contar_vizinhas(modelo_de_grade, i, j)

            if modelo_de_grade[i][j] == 0:
                if count == 3:
                    cell = 1
            elif modelo_de_grade[i][j] == 1:
                if count == 2 or count == 3:
                    cell = 1
            proxima_grade[i][j] = cell
    temp = modelo_de_grade
    modelo_de_grade = proxima_grade
    proxima_grade = temp


def contar_vizinhas(grade, linha, coluna):
    count = 0
    if linha-1 >= 0:
        count = count + grade[linha-1][coluna]
    if (linha - 1 >= 0) and (coluna - 1 >= 0):
        count += grade[linha-1][coluna-1]
    if (linha - 1 >= 0) and (coluna+1 < largura):
        count += grade[linha-1][coluna+1]
    if coluna - 1 >= 0:
        count += grade[linha][coluna-1]
    if coluna + 1 < largura:
        count += grade[linha][coluna+1]
    if linha + 1 < altura:
        count += grade[linha+1][coluna]
    if (linha + 1 < altura) and (coluna - 1 >= 0):
        count += grade[linha+1][coluna-1]
    if (linha + 1 < altura) and (coluna + 1 < largura):
        count += grade[linha+1][coluna +1]
    return count


glider_gun_pattern = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
              [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

glider_pattern = [[0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0],
                  [0, 0, 0, 1, 0],
                  [0, 1, 1, 1, 0],
                  [0, 0, 0, 0, 0]]


def load_pattern(pattern, x_offset=0, y_offset=0):
    global modelo_de_grade

    for i in range(0, altura):
        for j in range(0, largura):
            modelo_de_grade[i][j] = 0

    j = y_offset

    for row in pattern:
        i = x_offset
        for value in row:
            modelo_de_grade[i][j] = value
            i += 1
        j += 1


if __name__ == '__main__':
    next_gen()


