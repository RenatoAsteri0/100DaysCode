import requests
import datetime
import os
from dotenv import find_dotenv, load_dotenv

MEU_PESO = '77'
MINHA_ALTURA = '168'
IDADE = '23'
doentv_path = find_dotenv()
load_dotenv(doentv_path)

nutrition_headers = {
    'x-app-id': os.getenv('API_ID'),
    'x-app-key': os.getenv('API_KEY')
}
exercice = 'i ran for 10 miles'
nutrition_params = {
    'query': exercice,
    'weight_kg': MEU_PESO,
    'height_cm': MINHA_ALTURA,
    'age': IDADE
}
nutrition_url = 'https://trackapi.nutritionix.com/v2/natural/exercise'

nutrition_response = requests.post(url=nutrition_url, json=nutrition_params, headers=nutrition_headers)
result = nutrition_response.json()

hoje = datetime.datetime.now()
time = hoje.time().strftime('%H:%M:%S')
data = hoje.date().strftime('%Y-%m-%d')
googleshets_url = 'https://api.sheety.co/998db4b1cd9676aab0abe91eb37faacb/meusExercicios/workouts'


barear_auth = {
    "Authorization": 'Bearer renatotoken'
}
for exercices in result['exercises']:
    googleshets_colums = {
        'workout': {
            'date': data,
            'time': time,
            'exercice': exercices['name'],
            'duration': exercices['duration_min'],
            'calories': exercices['nf_calories']
        }
    }
    exercice_response = requests.post(url=googleshets_url, json=googleshets_colums, headers=barear_auth)
