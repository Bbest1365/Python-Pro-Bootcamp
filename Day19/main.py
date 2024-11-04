from turtle import Turtle, Screen
import random
screen = Screen()
screen.screensize(500,400)
user_bet = screen.textinput(title = "Make your bet", prompt="Which turtle will win the race ? Enter a color: ")
colors = ["red",'blue','green','yellow','black','purple']
tao = ['tao1','tao2','tao3','tao4','tao5','tao6']
j = 200
for index in range(0,6):
    tao[index] = Turtle()
    tao[index].shape('turtle')
    tao[index].shapesize(2)
    tao[index].color(colors[index])
    tao[index].penup()
    tao[index].goto(-500,j)
    j -= 100

if user_bet:
    is_race_on = True
while is_race_on:
    for tao_name in tao:
        if tao_name.xcor() > 480:
            is_race_on = False
            winning_color = tao_name.pencolor()
            if user_bet == winning_color:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 100)
        tao_name.forward(random_distance)









screen.exitonclick()

