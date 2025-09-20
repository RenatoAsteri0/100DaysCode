import requests
from dotenv import load_dotenv
import os

load_dotenv()
SHEETY_PRICES_ENDPOINT = 'https://api.sheety.co/998db4b1cd9676aab0abe91eb37faacb/flightDeals/prices'

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.headers = {'Authorization': os.getenv('APIBearer_Sheety')}
        self.destination_data = {}

    def get_sheed_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.headers)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def put_sheet_data(self):
        for city in self.destination_data:
            new_data = {
                'price': {
                    'iataCode': city['iataCode']
                }
            }
            response = requests.put(f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", headers=self.headers, json=new_data)
            print(response.text)