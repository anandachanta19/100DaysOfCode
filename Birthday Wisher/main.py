import smtplib
import datetime as dt
import random

my_email = "p116ff@gmail.com"
password = "nwaq pnxb pjay bqpz"

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 5:
    try:
        with open("quotes.txt", "r") as file:
            data = file.readlines()
    except FileNotFoundError:
        print("No File Found")
    else:
        quote = random.choice(data)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="venkatanand36@gmail.com",
                msg=f"Subject:Quote of the Day\n\n{quote}"
            )
