import os
from dotenv import load_dotenv
import requests
from datetime import datetime as dt

load_dotenv()

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
APP_ID = os.environ["NUTRITIONIX_APP_ID"]
API_KEY = os.environ["NUTRITIONIX_API_KEY"]
MY_WEIGHT = 68  # KG
MY_HEIGHT = 168  # CM
AGE = 19  # YEARS
SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]

EXERCISE_HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}

SHEETY_HEADERS = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

parameters = {
    "query": input("Tell me what exercises you have done today?"),
    "weight_kg": MY_WEIGHT,
    "height_cm": MY_HEIGHT,
    "age": AGE,
}

response = requests.post(url=EXERCISE_ENDPOINT, json=parameters, headers=EXERCISE_HEADERS)
response.raise_for_status()
data = response.json()["exercises"]
for exercise in data:
    sheet_params = {
        "workout": {
            "date": f"{dt.now().strftime("%d/%m/%Y")}",
            "time": f"{dt.now().strftime("%H:%M:%S")}",
            "exercise": f"{exercise["name"]}",
            "duration": f"{exercise["duration_min"]}",
            "calories": f"{exercise["nf_calories"]}",
        }
    }
    sheet_response = requests.post(
        url=SHEETY_ENDPOINT,
        json=sheet_params,
        headers=SHEETY_HEADERS,
    )
    sheet_response.raise_for_status()
