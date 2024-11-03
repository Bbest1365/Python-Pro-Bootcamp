import turtle as t
import random
tim = t.Turtle()

colors = ["green yellow","cyan","magenta","yellow","deep sky blue","deep pink","red","blue violet"]

angle = [0,90,180,270]
loop = True
tim.pensize(15)
tim.speed("fastest")
while loop:
    tim.color(random.choice(colors))
    tim.forward(40)
    direction = random.choice(angle)
    tim.setheading(direction)