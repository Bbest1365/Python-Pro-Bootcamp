import turtle as t
import random
t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color
def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(150)
        tim.right(size_of_gap)

draw_spirograph(20)







screen = t.Screen()
screen.exitonclick()
