import random
import turtle

Redie = turtle.Turtle()
Greenie = turtle.Turtle()
Pinkie = turtle.Turtle()
Yelly = turtle.Turtle()
Blu = turtle.Turtle()

screen = turtle.Screen()
screen.setup(1290, 720)
screen.bgpic('pavement.gif')
turtles = [Redie, Blu, Yelly, Pinkie, Greenie]
names = ['Redie', 'Blu', 'Yelly', 'Pinkie', 'Greenie']
positions = [-40, -20, 0, 20, 40]
colors = ['red', 'blue', 'yellow', 'pink', 'white']

for i in range(0, 5):
    turtles[i] = turtle.Turtle()
    turtles[i].color(colors[i])
    turtles[i].shape('turtle')
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

print(winner_name[0], 'é a vencedora')
