# Randomization

# project: Rock-Paper-scissors

import random


rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
choices = [rock, paper, scissors]
print(
    """
    ----------------------------------------------------------------
    ---------------- Let's Play Rock-Paper-Scissors ----------------
    ----------------------------------------------------------------
"""
)
my_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
)
if my_choice not in range(0, 3):
    print("Invalid number choice - Please choose 0, 1 or 2")
else:
    print(choices[my_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(choices[computer_choice])

    if my_choice == 0:
        if computer_choice == 2:
            print("You win 👏👏")
        elif computer_choice == my_choice:
            print("It's a draw 🟰🟰")
        else:
            print("You lose 🚫🚫")
    elif my_choice == 1:
        if computer_choice == 0:
            print("You win 👏👏")
        elif computer_choice == my_choice:
            print("It's a draw 🟰🟰")
        else:
            print("You lose 🚫🚫")
    elif my_choice == 2:
        if computer_choice == 1:
            print("You win 👏👏")
        elif computer_choice == my_choice:
            print("It's a draw 🟰🟰")
        else:
            print("You lose 🚫🚫")
    else:
        print("Invalid number choice!")
