import turtle
import random

slowpoke = turtle.Turtle()
turtle.register_shape('Sem título.gif')
slowpoke.shape('Sem título.gif')
slowpoke.color('blue')

pokie = turtle.Turtle()
pokie.shape('turtle')
pokie.color('red')

def color_change(the_turtle):
    colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink']
    color = random.choice(colors)
    the_turtle.penup
    the_turtle.pencolor(color)
    the_turtle.pendown
    
i = 0
def make_square(the_turtle):
    for i in range(0,4):
        the_turtle.forward(100)
        the_turtle.right(90)
        i += i
def make_spiral(the_turtle, function):
    for i in range(0,36):
        function(the_turtle)
        the_turtle.right(10)


def make_star(the_turtle):
     for i in range(5):
         the_turtle.forward(100)
         the_turtle.right(144)

def make_circle(the_turtle):
    the_turtle.circle(50)

def screen(the_turtle):
    positions = list(range(0,400))
    i = 0
    while i < 99:
        numberx = random.randint(-300,300)
        numbery = random.randint(-300,300)
        make_circle(the_turtle)
        the_turtle.setposition(numberx,numbery)
        color_change(the_turtle)
        make_spiral(the_turtle, make_square)
        the_turtle.setposition(-numberx,numbery)
        make_star(the_turtle)
        the_turtle.setposition(numbery, numberx)
        color_change(the_turtle)
        make_spiral(the_turtle, make_star)
        color_change(the_turtle)
        the_turtle.setposition(-numbery, -numberx)
        i += 1



screen(slowpoke)

turtle.mainloop()