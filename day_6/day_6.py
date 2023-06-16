# Functions, Code Blocks and While Loops

# Project:
"""
Lost in a maze
Reeborg was exploring a dark maze and the battery in its flashlight ran out.

# Go to the link below
http://reeborg.ca/reeborg.html?lang=en&mode=python&menu=%2Fworlds%2Fmenus%2Fselect_collection_en.json&name=Alone&url=%2Fworlds%2Ftutorial_en%2Falone.json
- And import the json files by cliking on Additional Options and then Open world from file (3 json files for 3 scenarios)

# Instructions
Write a program using an if/elif/else statement so Reeborg can find the exit. The secret is to have Reeborg follow along the right edge of the maze, turning right if it can, going straight ahead if it can't turn right, or turning left as a last resort.

# What you need to know
- The functions move() and turn_left().
- Either the test front_is_clear() or wall_in_front(), right_is_clear() or wall_on_right(), and at_goal().
- How to use a while loop and if/elif/else statements.
- It might be useful to know how to use the negation of a test (not in Python).



A robot located at (x, y) = (3, 4) carries no objects.

# Goal to achieve:
The final position of the robot must be (x, y) = (6, 4)
"""

## Solution


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    if right_is_clear() and front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()


while not at_goal():
    jump()
