# Challenge: Make a spirograph each with a radius of 100 with different colors.

import turtle as t
import random

# get random colors
t.colormode(255)


def get_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


tim = t.Turtle()
tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(get_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)


screen = t.Screen()
screen.exitonclick()
