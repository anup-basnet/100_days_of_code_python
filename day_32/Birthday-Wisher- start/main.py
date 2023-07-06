import smtplib
import datetime as dt
import pandas as pd
import random


##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


MY_EMAIL = "anupbasnet97@outlook.com"
PASSWORD = "#wrongPassword!"
PLACEHOLDER = "[NAME]"


# def wish_birthday(email, letter_body):
#     with smtplib.SMTP(
#         host="smtp-mail.outlook.com", port=587, timeout=120
#     ) as connection:
#         connection.starttls()
#         connection.login(user=MY_EMAIL, password=PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=email,
#             msg=f"Subject:Birthday\n\n{letter_body}",
#         )


# now = dt.datetime.now()
# month = now.month
# day = now.day


# df = pd.read_csv("birthdays.csv")
# for index, row in df.iterrows():
# if row.month == month and row.day == day:
#     letter_num = random.randint(1, 3)

#     with open(f"./letter_templates/letter_{letter_num}.txt") as letter:
#         original_letter = letter.read()
#         letter_to_send = original_letter.replace(PLACEHOLDER, row.person)

#     wish_birthday(row.email, letter_to_send)


###### METHOD - 2
today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pd.read_csv("birthdays.csv")

birthdays_dict = {
    (data_row["month"], data_row["day"]): data_row
    for (index, data_row) in data.iterrows()
}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents.replace(PLACEHOLDER, birthday_person["person"])

    with smtplib.SMTP(
        host="smtp-mail.outlook.com", port=587, timeout=120
    ) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Birthday\n\n{contents}",
        )
