import os
from twilio.rest import Client
import smtplib


class NotificationManager:

    def __init__(self):
        self.email = os.getenv("MY_EMAIL")
        self.password = os.getenv("MY_EMAIL_APP_PASSWORD")

    @staticmethod
    def send_message(flight_info):
        account_sid = os.getenv("TWILIO_SID")
        auth_token = os.getenv("TWILIO_TOKEN")
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(body=f"Low Price Alert! Only ₹{flight_info.price} to fly from {flight_info.origin_airport}"
                         f" to {flight_info.destination_airport}, on {flight_info.out_date} "
                         f"until {flight_info.return_date}",
                    from_=os.getenv("TWILIO_PHONE_NUMBER"),
                    to=os.getenv("MY_PHONE_NUMBER"))
        print(message.status)
        print(message.sid)

    def send_emails(self, to, flight_info):
        if flight_info.stops == 1:
            flight_type = "It's a Direct Flight"
        else:
            flight_type = "It is not a direct flight!"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)
            connection.sendmail(
                from_addr=self.email,
                to_addrs=to,
                msg=f"Subject:Low Flight Price Alert!\n\n"
                    f"Low Price Alert! Only {flight_info.price} INR to fly from {flight_info.origin_airport}"
                    f" to {flight_info.destination_airport}, on {flight_info.out_date} until {flight_info.return_date}."
                    f" {flight_type}"
            )
