import os
from dotenv import load_dotenv
import requests

TOKEN_ENDPOINT_AUTH = 'https://test.api.amadeus.com/v1/security/oauth2/token'
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
        print(city_name)
        code = 'TESTING'
        return code