# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

invited_names = []
PLACEHOLDER = "[name]"

## Method 1
# with open("./Input/Names/invited_names.txt") as file:
#     names = file.readlines()
#     for name in names:
#         invited_names.append(name.strip())

# for name in invited_names:
#     # letter_to_send = []
#     with open("./Input/Letters/starting_letter.txt") as file:
#         contents = file.readlines()
#         name_format = contents[0]
#         contents[0] = name_format.replace(PLACEHOLDER, f"{name}")
#         letter_to_send = contents

#     with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
#         file.writelines(letter_to_send)


## Method 2
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(
            f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w"
        ) as completed_letter:
            completed_letter.write(new_letter)
