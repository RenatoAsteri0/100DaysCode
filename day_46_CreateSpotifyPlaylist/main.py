from bs4 import BeautifulSoup
import requests
import base64

# Using what you've learnt about BeautifulSoup, scrape the top 100 song titles on that date into a Python List

#viagem = str(input('Qual ano voce quer viajar? digite a data nesse formato YYYY '))

url = 'https://playback.fm/charts/top-100-songs/' + '2006'
response = requests.get(url)
web_page = response.text
soup = BeautifulSoup(web_page, 'html.parser')

find_name = soup.find_all(class_='song', itemprop="name")
find_position = soup.find_all('td')
name = [song.getText() for song in find_name]
position = [pos.getText(strip=True) for pos in find_position if pos.getText(strip=True).isdigit()]

songs = {n: p for n, p in zip(name, position)}

#-----------------------------------------------------------------
def get_token():
    client_id = '37bcaace6f7043cbaa5ab8afbf340096'
    client_secret = '59099165d6654cd4a9f8210ecb30009c'

    ENDPOINT = 'https://accounts.spotify.com/api/token'
    encodedData = base64.b64encode(bytes(f"{client_id}:{client_secret}", "ISO-8859-1")).decode("ascii")
    headers = {
        'Authorization': 'Basic '+encodedData,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'client_credentials'
    }

    response = requests.post(url=ENDPOINT, headers=headers, data=data)
    if response.status_code == 200:
        r = response.json()
        token = r['access_token']
        token_type = r['token_type']
        token_duration = r['expires_in']
        print(f'Token de Acesso requisitado com successo!')
        print(f'Tipo do Token: {token_type}')
        print(f'Disponibilidade do Token: {token_duration} segundos')
        with open('token.txt', 'w') as file:
            file.write(token)
            print('token salvo no arquivo token.txt')
    else:
        print(response.status_code)
        print('Não foi possível obter o token de acesso')

    return f'{token_type} {token}'
get_token()