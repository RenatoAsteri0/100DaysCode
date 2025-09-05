import requests

parameters = {
    'amount': 10,
    'type': 'boolean'
}

data = requests.get('https://opentdb.com/api.php', params=parameters)
data.raise_for_status()
json_format = data.json()
question_data = json_format['results']