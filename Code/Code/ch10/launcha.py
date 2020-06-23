import math, turtle

screen = turtle.Screen()
screen.setup(1100, 850)
screen.bgpic('backimage.gif')
screen.setworldcoordinates(-50, -25, 50, 25)

cannon = turtle.Turtle()
turtle.register_shape('cannon-clipartn.gif')
cannon.shape('cannon-clipartn.gif')
cannon.penup()
cannon.goto(-50, -20)
turtle.register_shape('PENCIn.gif')
writer = turtle.Turtle()
writer.pencolor('white')
writer.shape('PENCIn.gif')
writer.ht()
writer.penup()
writer.goto(-10, 10)
writer.penup()
writer.st()


def lancamento(ang, velocidade):
    global writer
    objeto = turtle.Turtle()
    objeto.shape('circle')
    objeto.shapesize(0.5)
    objeto.color('white')
    objeto.penup()
    objeto.ht()
    objeto.goto(-50, -20)
    objeto.pendown()
    angulo = math.radians(ang)
    seno = math.sin(angulo)
    cosseno = math.cos(angulo)
    tempo = 0.01
    tempo_maximo = float((2 * velocidade * seno) / 10)
    objeto.st()
    while tempo < tempo_maximo and objeto.ycor() >= -20:
        pos_y = -20 + float(((velocidade * seno) * tempo) - 5 * (tempo ** 2))
        pos_x = -50 + float((velocidade * cosseno) * tempo)
        objeto.setposition(pos_x, pos_y)
        tempo += 0.007
    dist = objeto.xcor() + 50
    frase = 'Distância percorrida: ' + str(round(dist, 2)) + ' metros'
    return frase

user_answer = ''
while user_answer != 'sim':
    writer.clear()
    writer.goto(-10, 10)
    a = int(input('Ângulo desejado: '))
    v = int(input('Velocidade do objeto: '))
    writer.write(lancamento(a, v),move=True, align='right', font=('Verdana', 12, 'normal'))
    user_answer = input('Encerrar programa? ')


turtle.bye()
turtle.mainloop()
