import random
from art import logo, vs
from game_data import data


def format_data(account):
    """Format the account data into printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, A_followers, B_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    if A_followers > B_followers:
        return guess == "A"
    else:
        return guess == "B"


# Display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    # Generate a random account
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    # Format the account data into printable format
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    # Check if user is correct
    A_follower_count = account_a["follower_count"]
    B_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, A_follower_count, B_follower_count)

    print("\033c", end="")
    print(logo)
    # Give user feedback on their guess.
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")
