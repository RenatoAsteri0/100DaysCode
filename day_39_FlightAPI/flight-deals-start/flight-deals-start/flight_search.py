import os
from dotenv import load_dotenv
import requests

TOKEN_ENDPOINT_AUTH = 'https://test.api.amadeus.com/v1/security/oauth2/token'
TOKEN_ENDPOINT_CITIES = 'https://test.api.amadeus.com/v1/reference-data/locations/cities'
TOKEN_ENDPOINT_FLIGHT = 'https://test.api.amadeus.com/v2/shopping/flight-offers'

load_dotenv()
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.environ["APIKey_Amadeus"]
        self._api_secret = os.environ["APISecret_Amadeus"]
        self._secret_token = self._get_new_token()

    def _get_new_token(self):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }

        response = requests.post(url=TOKEN_ENDPOINT_AUTH, headers=headers, data=body)
        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()["access_token"]

    def get_destination_code(self, city_name):
        headers = {
            'Authorization': f'Bearer {self._secret_token}',
        }
        params = {
            'keyword': city_name,
            "max": "2",
            "include": "AIRPORTS",
        }
        request = requests.get(url=TOKEN_ENDPOINT_CITIES, params=params, headers=headers)
        code = request.json()["data"][0]['iataCode']
        return code

    def check_flights(self, origin_city_code, destiny_city_code, from_data, data_to):
        headers = {
            'Authorization': f'Bearer {self._secret_token}',
        }
        params = {
            'originLocationCode': origin_city_code,
            'destinationLocationCode': destiny_city_code,
            'departureDate': from_data,
            'returnDate': data_to,
            'adults': 1,
            'nonStop': True,
            'currencyCode': 'GBP',
            'max': '10',
        }
        response = requests.get(url=TOKEN_ENDPOINT_FLIGHT, params=params, headers=headers)
        if response.status_code != 200:
            print(f'check_flights() response code: {response.status_code}')
            print('There was a problem with the flights search.\n'
                  'For details on status codes, check the API documentation.'
                  'https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api'
                  '-reference')
            return None
        return response.json()