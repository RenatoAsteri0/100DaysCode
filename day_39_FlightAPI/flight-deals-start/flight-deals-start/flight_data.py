class FlightData:
    #This class is responsible for structuring the flight data.
    pass

import requests

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = 'grant_type=client_credentials&client_id=4V5CuJpTO1EZlPlAfq0vcdCn3y598hrX&client_secret=0yIxWH9Cu6DJ0OMn'

response = requests.post('https://test.api.amadeus.com/v1/security/oauth2/token', headers=headers, data=data)
