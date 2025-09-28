import os
from dotenv import load_dotenv
import requests
from amadeus import Client, ResponseError

load_dotenv()
class FlightSearch(Client):
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        super().__init__(
            client_id = os.environ["APIKey_Amadeus"],
            client_secret = os.environ["APISecret_Amadeus"]

        )

    def get_destination_code(self, city_name: str):
        response = self.reference_data.locations.cities.get(keyword=city_name)
        return response.data[0]['iataCode']

    def check_flights(self, origin_city_code, destiny_city_code, from_data, data_to):

        try:
            response = self.shopping.flight_offers_search.get(
                            originLocationCode=origin_city_code,
                            destinationLocationCode=destiny_city_code,
                            departureDate=from_data.strftime("%Y-%m-%d"),
                            adults='1')
            return response.result
        except ResponseError as error:
            print(error)
'''
        headers = {
            'Authorization': f'Bearer {self._secret_token}',
        }
        params = {
            'originLocationCode': origin_city_code,
            'destinationLocationCode': destiny_city_code,
            'departureDate': from_data.strftime("%Y-%m-%d"),
            'returnDate': data_to,
            'adults': 1,
            'nonStop': True,
            'max': '20',
        }
        response = requests.get(url=TOKEN_ENDPOINT_FLIGHT, params=params, headers=headers)
        print(response.url)
        print(params)
        if response.status_code != 200:
            print(f'check_flights() response code: {response.status_code}')
            print('There was a problem with the flights search.\n'
                  'For details on status codes, check the API documentation.'
                  'https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api'
                  '-reference')
            return None
        return response.json()'''