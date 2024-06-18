import os
from dotenv import load_dotenv
import requests

load_dotenv()

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID = os.environ["NUTRITIONIX_APP_ID"]
API_KEY = os.environ["NUTRITIONIX_API_KEY"]
MY_WEIGHT = 68  # KG
MY_HEIGHT = 168  # CM
AGE = 19  # YEARS

HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}

parameters = {
    "query": input("Tell me what exercises you have done today?"),
    "weight_kg": MY_WEIGHT,
    "height_cm": MY_HEIGHT,
    "age": AGE,
}

response = requests.post(url=EXERCISE_ENDPOINT, json=parameters, headers=HEADERS)
print(response.json())
