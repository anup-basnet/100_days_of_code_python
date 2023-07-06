import datetime as dt
import smtplib
import random

# Working with DateTime

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(year)
print(day_of_week)

if year == 2023:
    print("Wear a face mask.")

date_of_birth = dt.datetime(year=2000, month=6, day=27)
print(date_of_birth)


# working with smtp
my_email = "anupbasnet97@outlook.com"
password = "WrongPassword!"


def send_quote(quote):
    with smtplib.SMTP("smtp-mail.outlook.com", port=587, timeout=120) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="anupbsnt97@gmail.com",
            msg=f"subject: Positivity Quote\n\n{quote}",
        )


now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 3:  # Replace with your current weekday to send mail
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)

    send_quote(quote)
