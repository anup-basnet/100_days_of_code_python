# Data Types | Numbers | Operations | Type Conversion | f-Strings

# project: Tip-Calculator

print("Welcome to the tip calculator.")

total = float(input("What was the total bill? $"))
tip_percent = int(
    input("What percentage tip would you like to give? 10, 12, or 15? "))
num_of_people = int(input("How many people to split the bill? "))

total_with_tip = total + total * (tip_percent / 100)
per_person = total_with_tip / num_of_people

print(f"Each person should pay: ${per_person:.2f}")
