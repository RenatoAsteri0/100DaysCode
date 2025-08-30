"""import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

print(longitude, latitude)
"""
MY_LAT = -23.090800
MY_LONG = -47.218000

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

from datetime import datetime
import requests
import re

response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()

data = response.json()
time_now = datetime.now()

sunrise = data['results']['sunrise']
sunrise = re.sub(r"[T+]", " ",sunrise)

print(sunrise)
print(time_now)