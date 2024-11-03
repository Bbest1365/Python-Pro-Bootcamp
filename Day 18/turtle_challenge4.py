# import turtle as t
# import random
# tim = t.Turtle()
#
# colors = ["green yellow","cyan","magenta","yellow","deep sky blue","deep pink","red","blue violet"]
#
# angle = [0,90,180,270]
# loop = True
# tim.pensize(15)
# tim.speed("fastest")
# while loop:
#     tim.color(random.choice(colors))
#     tim.forward(40)
#     direction = random.choice(angle)
#     tim.setheading(direction)

import turtle as t
import random

tim = t.Turtle()
angle = [0,90,180,270]
loop = True
tim.pensize(15)
tim.speed("fastest")
t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color

while loop:
    tim.color(random_color())
    tim.forward(40)
    direction = random.choice(angle)
    tim.setheading(direction)
