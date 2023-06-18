# Functions with Outputs, Docstrings

# Project: Calculator
from art import logo


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


# Add other operations but logo doesn't include these symbols for now.
# Exponential
def exponent(n1, n2):
    return n1**n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for operation in operations:
        print(operation)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number?: "))
        answer = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        decision = input(
            f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation or type 'c' to close the calculator: "
        )
        if decision == "y":
            num1 = answer
        elif decision == "n":
            should_continue = False
            calculator()
        else:
            should_continue = False
            print("Turning off the calculator!! \n")


calculator()
