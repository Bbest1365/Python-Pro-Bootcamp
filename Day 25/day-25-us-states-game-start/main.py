import pandas as pd
import turtle
import csv


screen = turtle.Screen()
my_turtle = turtle.Turtle()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
while True:
    answer_state = screen.textinput(title = "Guess the State", prompt="What's another state's name?")

    data = pd.read_csv('50_states.csv')

    for state in data['state']:
        if  state.lower() == answer_state.lower():
            true_state = data[data['state'] == state]
            x = true_state['x']
            y = true_state['y']
            my_turtle.penup()
            my_turtle.hideturtle()
            my_turtle.goto(int(x),int(y))
            my_turtle.write(state,align="center",font=("Arial",16,"normal"))





# screen.exitonclick()