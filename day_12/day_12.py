# Scopes

# Project: Number-Guessing-Game
import random
from art import logo

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5


def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        print("Guess again.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        print("Guess again.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = random.randint(1, 100)
    print(f"Psst, the solution is {answer}")

    turns = set_difficulty()

    guess = 0
    while guess != answer and turns > 0:
        print(f"You hanve {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses. You lose.")


game()
