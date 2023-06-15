# For Loops, Range and Code Blocks

# Project: Password Generator
import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3" "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password? \n"))
nr_symbols = int(input("How many symbols would you like in your password? \n"))
nr_numbers = int(input("How many numbers would you like in your password? \n"))

# Easy Level: letters + symbols + numbers in sequence
easy_password = ""
for i in range(nr_letters):
    easy_password += random.choice(letters)

for i in range(nr_symbols):
    easy_password += random.choice(symbols)

for i in range(nr_numbers):
    easy_password += random.choice(numbers)

print(f"Your password is: {easy_password}")


# Hard Level: random sequence
password_list = []
hard_password = ""
pwd_length = nr_letters + nr_symbols + nr_numbers

for i in range(nr_letters):
    password_list.append(random.choice(letters))

for i in range(nr_symbols):
    password_list.append(random.choice(symbols))

for i in range(nr_numbers):
    password_list.append(random.choice(numbers))

# print(password_list)
random.shuffle(password_list)

for char in password_list:
    hard_password += char

print(f"Your password is: {hard_password}")
