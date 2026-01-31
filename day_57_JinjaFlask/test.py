import requests
import os
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.getenv('AGIFY_GENDERIZE')
end_point = 'https://api.genderize.io'
parameters = {
    'name': 'renato',
    'country_id': 'US',
    'apikey': APIKEY
}

responde = requests.get(url=end_point, params=parameters)
print(responde)
