from turtle import Turtle, Screen
import random

is_race_on = False
# Set the screen to custom size
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(
    title="Make your bets",
    prompt="Which turtle will win the race? Enter a color:\n(red/orange/yellow/green/blue/purple)",
)
print(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = ["tim", "tom", "amy", "monty", "penny", "eva"]

for i in range(len(turtles)):
    turtles[i] = Turtle(shape="turtle")
    turtles[i].color(colors[i])
    turtles[i].penup()
    y_pos = -100 + i * 30
    turtles[i].goto(x=-230, y=y_pos)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(
                    f"""
                    ----------------------------------------------------
                    You've won! The {winning_color} turtle is the winner!
                    ----------------------------------------------------
                    """
                )
            else:
                print(
                    f"""
                    ----------------------------------------------------
                    You've lost.The {winning_color} turtle is the winner!
                    ----------------------------------------------------
                    """
                )
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
