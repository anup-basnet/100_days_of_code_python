"""
    List comprehension:
    new_list = [new_item for item in list]
"""

numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)


name = "Angela"
letters_list = [letter for letter in name]
print(letters_list)


range_list = [num * 2 for num in range(1, 5)]
print(range_list)


# Conditional List Comprehension
# new_list = [new_item for item in list if test/condition]

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) <= 4]
print(short_names)


# challenge: if name >= 5 letters turn into capital and make new list
capital_names = [name.upper() for name in names if len(name) > 4]
print(capital_names)


"""
    Dictionary Comprehension:
    new_dict = {
        new_key:new_value for (key, value) in dict.items() if test
        }
"""
import random

NAMES = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
students_scores = {student: random.randint(1, 100) for student in NAMES}
print(students_scores)

passed_students = {
    student: score for (student, score) in students_scores.items() if score > 50
}
print(passed_students)
