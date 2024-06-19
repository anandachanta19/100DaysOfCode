import requests
import os
from dotenv import load_dotenv

load_dotenv()


class DataManager:
    def __init__(self):
        self.endpoint = os.environ["SHEETY_ENDPOINT"]
        self.token = os.environ["SHEETY_BEARER_TOKEN"]

    def get_data(self):
        header = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url=self.endpoint, headers=header)
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

        put_url = self.endpoint + f"/{row_id}"
        response = requests.put(url=put_url, headers=header, json=parameters)
        response.raise_for_status()
