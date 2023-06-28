import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


df = pd.read_csv("50_states.csv")
all_states = df.state.to_list()


tim = turtle.Turtle()
guessed_states = []
states_remaining = []


# Check if the guess is among the 50 states

while len(guessed_states) < 50:
    if len(guessed_states) == 0:
        answer_state = screen.textinput(
            title=f"{len(guessed_states)} / 50 States Correct",
            prompt="Guess the states's name? ",
        ).title()
    else:
        answer_state = screen.textinput(
            title=f"{len(guessed_states)} / 50 States Correct",
            prompt="What's another states's name? \n( Type 'exit' to exit the game. )",
        ).title()

    if answer_state.lower() == "exit":
        for state in all_states:
            if state not in guessed_states:
                states_remaining.append(state)
        new_data = pd.DataFrame(states_remaining)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states and answer_state not in guessed_states:
        tim.penup()
        tim.hideturtle()
        state_data = df[df.state == answer_state]
        tim.goto(int(state_data.x), int(state_data.y))
        tim.write(f"{answer_state}")

        guessed_states.append(answer_state)


# screen.exitonclick()
