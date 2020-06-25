import random
import turtle
import time


screen = turtle.Screen()
screen.setup(1290, 720)
screen.bgpic('pavement.gif')
positions = [-200, -100, 0, 100, 200]
colors = ['red', 'blue', 'yellow', 'pink', 'white']
turtles = ['', '', '', '', '']
for i in range(0, 5):
    turtles[i] = turtle.Turtle()
    turtles[i].color(colors[i])
    turtles[i].shape('turtle')
    turtles[i].turtlesize(5)
    turtles[i].penup()
    turtles[i].setposition(-480, positions[i])
    turtles[i].pendown()


def move_turtle(t):
    n = random.randint(0, 9)
    t.forward(n)


winner = False

while not winner:
    for current_turtle in turtles:
        move_turtle(current_turtle)
        xcor = current_turtle.xcor()
        if xcor >= 590:
            winner = True
            winner_name = current_turtle.color()
            time.sleep(1)
for turtle_i in turtles:
    if turtle_i.color() != winner_name:
        turtle_i.hideturtle()
pencil = turtle.Turtle()
name = winner_name[0]
nomes = {'red': 'Vermelha', 'yellow': 'Amarela', 'pink': 'Rosa', 'blue': 'Azul',
         'white': 'Branca'}
arg = 'A Tartaruga ' + nomes[name] + ' é a vencedora!'
pencil.pencolor(name)
pencil.write(arg.upper(), move=False, align="center", font=("Gotham", 35, "normal"))
pencil.hideturtle()
screen.exitonclick()
            


