import requests

question_data = []
data = requests.get('https://opentdb.com/api.php?amount=10&type=boolean')
json_format = data.json()
question_data.append(json_format)

for a in question_data:
    print(a['results'][0]['category'])

categoria = [item['category'] for item in question_data[0]['results']]
print(categoria)