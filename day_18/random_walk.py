import turtle as t
import random

# TODO: challenge-4 : Draw a random walk in turtle graphics with random colors for each walk

tim = t.Turtle()
# change the color mode to rgb
t.colormode(255)

# change the size and speed of drawing
tim.pensize(8)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# east, north, west , south
directions = [0, 90, 180, 270]


for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

# show the screen until user clicks on it to exit
Screen = t.Screen()
Screen.exitonclick()
