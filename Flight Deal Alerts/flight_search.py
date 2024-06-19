import requests
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
CITY_SEARCH = "https://test.api.amadeus.com/v1/reference-data/locations/cities"


class FlightSearch:
    def __init__(self):
        self.api_key = os.environ["FLIGHT_API_KEY"]
        self.api_secret = os.environ["FLIGHT_API_SECRET"]
        self.token = self.get_new_token()

    def get_new_token(self):
        header = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self.api_key,
            'client_secret': self.api_secret
        }

        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)

        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']

    def get_iata_code(self, name: str) -> str:
        parameters = {
            "keyword": name,
            "max": 1
        }
        header = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url=CITY_SEARCH, params=parameters, headers=header)
        response.raise_for_status()
        return response.json()["data"][0]["iataCode"]

