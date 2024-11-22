from turtle import Turtle, Screen
import random
screen = Screen()
screen.screensize(500,400)
user_bet = screen.textinput(title = "Make your bet", prompt="Which turtle will win the race ? Enter a color: ")
colors = [
    "red", "blue", "green", "yellow", "black", "purple",
    "gold", "grey", "pink", "cyan", "magenta", "orange",
    "brown", "teal", "navy", "lavender", "coral", "turquoise",
    "salmon", "beige", "lime", "indigo", "violet", "peach",
    "chocolate", "crimson", "maroon", "mint", "khaki",
    "plum", "orchid", "tan", "auburn", "sapphire"
]
#max number_of_turtle_is 34

All_taos = []
j = 400
for index in range(0,9):
    tao = Turtle()
    tao.shape('turtle')
    tao.shapesize(2)
    tao.color(colors[index])
    tao.penup()
    tao.goto(-500,j)
    All_taos.append(tao)
    j -= 100

if user_bet:
    is_race_on = True
while is_race_on:
    for tao_name in All_taos:
        if tao_name.xcor() > 400:
            is_race_on = False
            winning_color = tao_name.pencolor()
            if user_bet == winning_color:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 100)
        tao_name.forward(random_distance)









screen.exitonclick()

