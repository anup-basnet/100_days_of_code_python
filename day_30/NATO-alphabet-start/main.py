# Error Handling for day_26 project

import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

# Method - 1
# valid_word = False
# while not valid_word:
#     word = input("Enter a word: ").upper()
#     try:
#         output_list = [nato_dict[letter] for letter in word]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#     else:
#         valid_word = True
#         print(output_list)


# Method - 2
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
