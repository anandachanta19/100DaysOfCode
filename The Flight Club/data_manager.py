import requests
import os
from dotenv import load_dotenv

load_dotenv()


class DataManager:
    def __init__(self):
        self.prices_endpoint = os.environ["SHEETY_PRICES_ENDPOINT"]
        self.users_endpoint = os.environ["SHEETY_USERS_ENDPOINT"]
        self.token = os.environ["SHEETY_BEARER_TOKEN"]

    def get_data(self):
        header = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url=self.prices_endpoint, headers=header)
        response.raise_for_status()
        print(response.json())
        return response.json()

    def put_iata(self, iata, row_id):
        header = {
            "Authorization": f"Bearer {self.token}"
        }

        parameters = {
            "price": {
                "iataCode": iata
            }
        }

        put_url = self.prices_endpoint + f"/{row_id}"
        response = requests.put(url=put_url, headers=header, json=parameters)
        response.raise_for_status()

    def get_customers_emails(self):
        header = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url=self.users_endpoint, headers=header)
        response.raise_for_status()
        print("Getting Users Data!...")
        print(response.json())
        return response.json()
