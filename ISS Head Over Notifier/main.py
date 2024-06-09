import requests

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


sunrise, sunset = get_sunrise_sunset()
curr_lat, curr_long = get_iss_location()
