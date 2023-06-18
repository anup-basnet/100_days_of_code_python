# Dictionaries & Nesting

# Project: Blind-Auction
from art import logo

print(logo)
print("Welcome to the secret auction program.")

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # {"ram": 225, "man": 453}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    next_bidder = input("Are there any other bidders? Type 'yes' or 'no'.").lower()

    # store the values in dictionary
    bids[name] = price

    if next_bidder == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif next_bidder == "yes":
        print("\033c", end="")  # clear the console to hide prev values
