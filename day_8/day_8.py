# Functions with inputs, arguments and parameters

# Project: Caesar-Cipher
from art import logo

print(logo)
alphabet = [
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
]

should_continue = True


def caesar(input_text, shift_amount, cipher_type):
    result = ""
    if cipher_type == "decode":
        shift_amount = -shift_amount

    for char in input_text:
        if not char in alphabet:  # modify only alphabets
            result += char
        else:
            position = alphabet.index(char)
            new_position = position + shift_amount
            if new_position > 25:
                result += alphabet[new_position % 26]
            elif new_position < -25:
                result += alphabet[new_position % -26]
            else:
                result += alphabet[new_position]

    print(f"The {cipher_type}d text is: {result}\n")


while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(input_text=text, shift_amount=shift, cipher_type=direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("Goodbye")
