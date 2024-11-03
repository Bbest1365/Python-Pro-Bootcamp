from turtle import Turtle, Screen

tao = Turtle()
tao.shape("turtle")
tao.color("red")

for i in range(4):
    tao.forward(200)
    tao.right(90)

screen = Screen()
screen.exitonclick()

