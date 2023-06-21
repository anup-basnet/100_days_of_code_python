# Modules: importing modules and Turtle Module

from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("red")

# tim.forward(100)
# tim.right(90)


# TODO: challenge-1: Draw the square 100 x 100
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)


# TODO: challenge-2: Draw a dashed line, move 10 paces then gap of 10 paces and repeat this 15 times
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()  # Pull the pen up – no drawing when moving.
#     tim.forward(10)
#     tim.pendown()  # Pull the pen down – drawing when moving.


# TODO: challenge-3: Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon ovelapping each with side 100
import random

shapes = {
    # shape: sides
    "triangle": 3,
    "square": 4,
    "pentagon": 5,
    "hexagon": 6,
    "heptagon": 7,
    "octagon": 8,
    "nonagon": 9,
    "decagon": 10,
}
colors = ["red", "blue", "green", "orange", "black", "cyan", "pink", "wheat"]

for shape in shapes:
    tim.color(random.choice(colors))
    turn = 360 / shapes[shape]
    for _ in range(shapes[shape]):
        tim.forward(100)
        tim.right(turn)


# show the screen until you click
screen = Screen()
screen.exitonclick()
