import requests
from twilio.rest import Client
import os

LATITUDE = 26.080130
LONGITUDE = 91.558411

account_sid = os.environ.get("TWILIO_SDI")
auth_token = os.environ.get("TWILIO_TOKEN")

# Open Weather API Key
WEATHER_API_KEY = os.environ.get("WEATHER_API")

weather_parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": WEATHER_API_KEY,
    "cnt": 4,
}

response = requests.get(
    url=f"https://api.openweathermap.org/data/2.5/forecast",
    params=weather_parameters
)
response.raise_for_status()
weather_data = response.json()
will_rain = False
for data in weather_data["list"]:
    for weather in data["weather"]:
        if weather["id"] < 700:
            will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(body="It's going to rain today. So don't forget to bring an ☔", from_=os.environ.get("FROM"),
                to=os.environ.get("TO"))
