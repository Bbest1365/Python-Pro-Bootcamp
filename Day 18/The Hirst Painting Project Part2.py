import turtle as t
import random
color_list = [(254, 254, 253), (228, 0, 87), (246, 254, 252), (126, 87, 59), (48, 170, 224), (47, 172, 102), (197, 189, 17), (235, 220, 0), (191, 229, 249), (254, 247, 252), (209, 202, 148), (235, 110, 145), (102, 192, 187), (227, 25, 114), (233, 78, 28), (1, 72, 148), (219, 176, 69), (226, 42, 121), (13, 79, 148), (244, 159, 193), (47, 160, 201), (155, 212, 192), (143, 209, 230), (8, 59, 110), (56, 148, 98), (241, 173, 153), (90, 129, 170), (159, 194, 229), (253, 4, 79), (77, 59, 48)]
t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
i=0
tim.hideturtle()
tim.penup()
def walk():
    for i in range(10):
        tim.dot(30,random.choice(color_list))
        tim.forward(100)

for way in range(10):
    tim.goto(-500, i)
    walk()
    i+=50










screen = t.Screen()
screen.exitonclick()




