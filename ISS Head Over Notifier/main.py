import datetime as dt
import smtplib

import requests

EMAIL = "p116ff@gmail.com"
PASS = "sfeq ntof hebl gfls"

LATITUDE = 26.080130
LONGITUDE = 91.558411
parameters = {
    "lat": LATITUDE,
    "lng": LONGITUDE,
    "formatted": 0,
    "tzid": "Asia/Kolkata",
}


# returns Sunrise and Sunset
def get_sunrise_sunset():
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sr_list = data["results"]["sunrise"].split("T")
    sr = sr_list[1].split("+")[0]
    ss_list = data["results"]["sunset"].split("T")
    ss = ss_list[1].split("+")[0]
    return sr, ss


# returns iss position
def get_iss_location():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    return data["iss_position"]["latitude"], data["iss_position"]["longitude"]


# returns true if iss is close
def is_close(lat, long):
    if LATITUDE - 5 <= lat <= LATITUDE + 5 and LONGITUDE - 5 <= long <= LONGITUDE + 5:
        return True
    else:
        return False


sunrise_time, sunset_time = get_sunrise_sunset()
iss_lat, iss_long = get_iss_location()
current_time = dt.datetime.now()
# getting hours minutes seconds separated
now = str(current_time).split(":")
sunrise = sunrise_time.split(":")
sunset = sunset_time.split(":")

if is_close(float(iss_lat), float(iss_long)):
    if now[0] > sunset[0] or now[0] < sunrise[0]:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASS)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs="anandachanta19@gmail.com",
                msg="Subject:Look into the Sky!!!\n\n"
                    "ISS is flying above in the sky at your location"
            )
