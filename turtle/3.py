import turtle
import random
from turtle import *

a = turtle.Turtle()
a.hideturtle()
a.speed(0)
a.width(5)

colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange', 'black']

def up():
    a.setheading(90)
    a.forward(100)

def down():
    a.setheading(270)
    a.forward(100)

def left():
    a.setheading(180)
    a.forward(100)

def right():
    a.setheading(0)
    a.forward(100)

def clickleft(x, y):
    a.color(random.choice(colors))

def clickright(x, y):
    a.stamp()

turtle.listen()

turtle.onscreenclick(clickleft, 1)
turtle.onscreenclick(clickright, 3)

turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')

turtle.mainloop()
