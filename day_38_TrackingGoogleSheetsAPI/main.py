import requests

MEU_PESO = '77'
MINHA_ALTURA = '168'
IDADE = '23'

nutrition_headers = {
    'x-app-id': '83055098',
    'x-app-key': 'd0e238bb164069a3cf5aea95f40d4b0e'
}
exercice = input('digite quais exercicios voce fez: ')
nutrition_params = {
    'query': exercice,
    'weight_kg': MEU_PESO,
    'height_cm': MINHA_ALTURA,
    'age': IDADE
}
nutrition_url = 'https://trackapi.nutritionix.com/v2/natural/exercise'

response = requests.post(url=nutrition_url, json=nutrition_params, headers=nutrition_headers)
print(response.json())