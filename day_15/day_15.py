# Project: Coffe-Machine


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def format_resources():
    """Formats the resources available in printable form"""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]

    print(f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g \nMoney: ${money}")


def check_resources(order):
    """Takes the resources available as input and returns True if the resources are sufficient to make the drink ordered."""
    drink = MENU[order]["ingredients"]
    for item in drink:
        if resources[item] < drink[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def update_resources(order):
    """Takes the resources available as input and returns the updated quantity of resources after making the drink ordered."""
    # water_before = resources["water"]
    # milk_before = resources["milk"]
    # coffee_before = resources["coffee"]

    # drink = MENU[order]["ingredients"]
    # water_used = drink["water"]
    # milk_used = drink["milk"]
    # coffee_used = drink["coffee"]

    # water_remaining = water_before - water_used
    # milk_remaining = milk_before - milk_used
    # coffee_remaining = coffee_before - coffee_used

    # return {
    #     "water": water_remaining,
    #     "milk": milk_remaining,
    #     "coffee": coffee_remaining,
    # }

    drink = MENU[order]["ingredients"]
    ingredients = {}

    for ingredient in drink:
        ingredient_before = resources[ingredient]
        ingredient_used = drink[ingredient]
        ingredient_remaining = ingredient_before - ingredient_used
        ingredients[ingredient] = ingredient_remaining

    return ingredients


money = 0
drinks = ["espresso", "latte", "cappuccino"]
is_machine_on = True

while is_machine_on:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "report":
        format_resources()
    elif order in drinks:
        resources_sufficient = check_resources(order)
        if resources_sufficient:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))

            total_coins = (
                quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
            )

            total_amount = float(MENU[order]["cost"])

            change = total_coins - total_amount

            if change < 0:
                print("Sorry, that's not enough money. Money refunded.")
            else:
                print(f"Here is ${change:.2f} in change.")
                print(f"Here is your {order} ☕ Enjoy!")

                resources = update_resources(order)
                # format_resources()
                money += total_amount
    elif order == "off":
        is_machine_on = False
    else:
        print("Please select the drinks shown above.")
