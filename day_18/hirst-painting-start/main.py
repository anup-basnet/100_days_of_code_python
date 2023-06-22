# import colorgram
import turtle as t
import random

# Extract the colors from the hrist painting image
# colors = colorgram.extract("image.jpg", 6)
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

# Get the colors list from above print and delete the background colors
color_list = [
    (202, 164, 110),
    (240, 245, 241),
    (236, 239, 243),
    (149, 75, 50),
    (222, 201, 136),
    (53, 93, 123),
    (170, 154, 41),
    (138, 31, 20),
    (134, 163, 184),
    (197, 92, 73),
    (47, 121, 86),
    (73, 43, 35),
    (145, 178, 149),
    (14, 98, 70),
    (232, 176, 165),
    (160, 142, 158),
    (54, 45, 50),
    (101, 75, 77),
    (183, 205, 171),
    (36, 60, 74),
    (19, 86, 89),
    (82, 148, 129),
    (147, 17, 19),
    (27, 68, 102),
    (12, 70, 64),
    (107, 127, 153),
    (176, 192, 208),
    (168, 99, 102),
]

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")


def get_color():
    return random.choice(color_list)


tim.penup()
tim.hideturtle()
# Change the starting position from centre to include 10 dots in screen
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

# Create a 10 x 10 area to include 10 dots on each side with different colors at ad distance of 50
for _ in range(10):
    for _ in range(10):
        tim.dot(20, get_color())
        tim.forward(50)

    tim.setheading(180)
    tim.forward(500)
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(0)


# Screen
screen = t.Screen()
screen.exitonclick()
