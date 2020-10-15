import turtle
import random

a = turtle.Turtle()
colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange', 'black']

# set colors for turtle: red => outline, green => fill
a.color('red', 'blue')

# set pen width
a.width(5)

# Fill in shape will color
a.begin_fill()
a.circle(50)
a.end_fill()

a.penup()
a.forward(100)
a.pendown()

a.color('yellow', 'black')

a.begin_fill()
for x in range(4):
    a.forward(100)
    a.right(90)
a.end_fill()

for x in range(5):
    randColor = random.randrange(0, len(colors))
    a.color(colors[randColor], colors[random.randrange(0, len(colors))])
    rand1 = random.randrange(-300, 300)
    rand2 = random.randrange(-300, 300)
    a.penup()
    a.setpos((rand1, rand2))
    a.pendown()
    a.begin_fill()
    a.circle(random.randrange(0,80))
    a.end_fill()