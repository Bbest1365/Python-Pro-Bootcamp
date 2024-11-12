import pandas as pd
import turtle
import csv


screen = turtle.Screen()
my_turtle = turtle.Turtle()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv('50_states.csv')
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title = f"{len(guessed_states)}/50 Status Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
                #### [new_item for item in list if test]
        missing_states = [state for state in all_states if state not in guessed_states]
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")

        break

    for state in data['state']:
        if  state == answer_state:
            true_state = data[data['state'] == state]
            x = true_state['x'].item()
            y = true_state['y'].item()
            my_turtle.penup()
            my_turtle.hideturtle()
            my_turtle.goto(x,y)
            my_turtle.write(state)
            guessed_states.append(state)

# States to learn.csv






# screen.exitonclick()