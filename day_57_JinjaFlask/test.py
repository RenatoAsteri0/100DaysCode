import requests
import os
from dotenv import load_dotenv

load_dotenv()
end_point = 'https://api.genderize.io'
parameters = {
    'name': 'renato',
    'country_id': 'US'
}

responde = requests.get(url=end_point, params=parameters)
print(responde.json()['gender'])
