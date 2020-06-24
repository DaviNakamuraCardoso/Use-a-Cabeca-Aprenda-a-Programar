import requests
import json
import turtle

screen = turtle.Screen()
screen.setup(1000, 500)
screen.bgpic('earth.gif')
screen.setworldcoordinates(-180, -90, 180, 90)

url = 'http://api.open-notify.org/iss-now.json'
response = requests.get(url)
text = json.loads(response.text)
latitude = float(text["iss_position"]["latitude"])
longitude = float(text["iss_position"]["longitude"])
iss = turtle.Turtle()
turtle.register_shape('iss.gif')
iss.shape('iss.gif')
iss.turtlesize(0.25)
iss.penup()
iss.setposition(longitude, latitude)
iss.pendown()

while 0 < 1:
    url = 'http://api.open-notify.org/iss-now.json'
    response = requests.get(url)
    text = json.loads(response.text)
    latitude = float(text["iss_position"]["latitude"])
    longitude = float(text["iss_position"]["longitude"])
    iss.pendown()
    if iss.xcor() >= 178:
        iss.penup()
    iss.setposition(longitude, latitude)


turtle.mainloop()

