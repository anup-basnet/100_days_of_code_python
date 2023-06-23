# Higher Order Function: Passing function as input to another function

from turtle import Turtle, Screen

"""
# Challenge: Move the turtle on pressing the keys as follows
w - forward
s - backward
a - counter-clockwise
d - clockwise
c - clear the drawing
"""

tim = Turtle()


screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def move_counter_clockwise():
    tim.setheading(tim.heading() + 10)


def move_clockwise():
    tim.setheading(tim.heading() - 10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
