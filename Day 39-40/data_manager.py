import os
import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]

        self.prices_endpoint = os.environ["SHEETY_PRICES_ENDPOINT"]
        self.users_endpoint = os.environ["SHEETY_USERS_ENDPOINT"]
        self.authorization = HTTPBasicAuth(self._user, self._password) # Basic Authorization
        self.destination_data = []
        self.customer_data = {}


    def get_destination_data(self):
        response = requests.get(self.prices_endpoint, auth=self.authorization)
        response.raise_for_status()
        self.destination_data = response.json()["prefs"]
        return self.destination_data


    def update_codes(self):
        for city in self.destination_data:
            new_iata = {
                "pref": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{self.prices_endpoint}/{city["id"]}", json=new_iata, auth=self.authorization)
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(self.users_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data


