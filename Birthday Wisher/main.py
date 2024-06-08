import smtplib
import datetime as dt
import pandas
import random
MY_EMAIL = "p116ff@gmail.com"
PASSWORD = "nwaq pnxb pjay bqpz"

now = dt.datetime.now()
month = now.month
day = now.day

dob = pandas.read_csv("birthdays.csv")
data = dob.to_dict(orient="records")
for entry in data:
    if (month, day) == (entry["month"], entry["day"]):
        try:
            with open(f"letter_templates/letter_{random.randint(1, 3)}.txt", "r") as file:
                letter = file.read()
        except FileNotFoundError:
            print("There is no file found")
        else:
            updated_letter = letter.replace("[NAME]", f"{entry["name"]}")
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=f"{entry["email"]}",
                    msg=f"Subject:Happy Birthday!\n\n{updated_letter}"
                )
