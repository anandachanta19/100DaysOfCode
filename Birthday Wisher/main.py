import smtplib
import datetime as dt
import random

MY_EMAIL = "p116ff@gmail.com"
PASSWORD = "nwaq pnxb pjay bqpz"

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 0:
    try:
        with open("quotes.txt", "r") as file:
            data = file.readlines()
    except FileNotFoundError:
        print("No File Found")
    else:
        quote = random.choice(data)
        print(quote)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="venkatanand36@gmail.com",
                msg=f"Subject:Monday Motivation\n\n{quote}"
            )
