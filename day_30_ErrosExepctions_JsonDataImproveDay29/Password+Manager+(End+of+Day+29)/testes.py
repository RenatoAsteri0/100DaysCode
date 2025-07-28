import json
with open('data.json', 'r') as data_file:
    data = json.load(data_file)

    for _ in data:
        if data['teste']['password'] == 'P%SzHrn21i+3k0V':
            email = data['teste']['email']
            print(email)