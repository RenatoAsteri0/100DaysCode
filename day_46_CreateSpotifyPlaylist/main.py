from bs4 import BeautifulSoup
import requests
import base64
import os
from dotenv import load_dotenv
import urllib.parse
import webbrowser
import random
import string

load_dotenv()
CLIENT_ID = os.getenv('client_id')
CLIENT_SECRET = os.getenv('client_secret')
USER_ID = os.getenv('user_id')
REDIRECT_URI = os.getenv('redirect_url')
AUTH_TOKEN = os.getenv('auth_token')
STATE = os.getenv('state')

# Using what you've learnt about BeautifulSoup, scrape the top 100 song titles on that date into a Python List

def get_songs():
    url = 'https://playback.fm/charts/top-100-songs/' + '2006'
    response = requests.get(url)
    web_page = response.text
    soup = BeautifulSoup(web_page, 'html.parser')

    find_name = soup.find_all(class_='song', itemprop="name")
    find_position = soup.find_all('td')
    name = [song.getText() for song in find_name]
    position = [pos.getText(strip=True) for pos in find_position if pos.getText(strip=True).isdigit()]

    songs = {n: p for n, p in zip(name, position)}
    return songs
def get_auth_token(client_id, redirect_uri):

    # 🔐 Dados da aplicação
    scope = 'user-read-private user-read-email'

    # 🔒 Gera um estado aleatório para segurança
    def generate_state(length=16):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    state = generate_state()

    # 🔗 Monta a URL de autorização
    params = {
        'response_type': 'code',
        'client_id': client_id,
        'scope': scope,
        'redirect_uri': redirect_uri,
        'state': state,
        'show_dialog': 'true'
    }

    auth_url = 'https://accounts.spotify.com/authorize?' + urllib.parse.urlencode(params)
    print(params['redirect_uri'])
    # 🌐 Abre a URL no navegador para o usuário autorizar
    webbrowser.open(auth_url)

    print("Abra o navegador se não abriu automaticamente.")
    print("Após autorizar, copie o código da URL de redirecionamento.")
def get_token(code, redirect_url, client_id, client_secret):
    ENDPOINT = 'https://accounts.spotify.com/api/token'
    base64_auth = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()

    headers = {
        'Authorization': f'Basic {base64_auth}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_url
    }

    response = requests.post(url=ENDPOINT, headers=headers, data=data)

    if response.status_code == 200:
        r = response.json()
        token = r['access_token']
        token_type = r['token_type']
        token_duration = r['expires_in']
        print('✅ Token de acesso requisitado com sucesso!')
        print(f'Tipo do Token: {token_type}')
        print(f'Duração: {token_duration} segundos')

        with open('token.txt', 'w') as file:
            file.write(token)
            print('💾 Token salvo em token.txt')

        return f'{token_type} {token}'
    else:
        print(f'❌ Erro {response.status_code}: Não foi possível obter o token')
        print(response.text)
        return None

def get_user_id(token_basic):
    ENDPOINT = 'https://api.spotify.com/v1/me'
    print(token_basic)

    headers = {
        'Authorization':token_basic
    }
    response = requests.get(url=ENDPOINT, headers=headers)
    print(response.url)
    return response.json()
def create_playlist(user_id, token_playlist):
    ENDPOINT = f'https://api.spotify.com/v1/users/{user_id}/playlists'
    headers = {
        'Authorization': 'Bearer '+token_playlist,
        'Content-Type': 'application/json'
    }
    print(headers['Authorization'])
    data = {
        "name": "nostalgic",
        "description": "day 46",
        "public": 'false'
    }
    response = requests.post(url=ENDPOINT, headers=headers, data=data)

    if response.status_code == 200:
        print('playlist criada com sucesso')
        print(response)
        print(response.text)
        print(response)
    else:
        print('falha')
        print(response)
        print(response.text)
        print(response.url)

#get_auth_token(CLIENT_ID,REDIRECT_URI)
#get_token(AUTH_TOKEN, REDIRECT_URI, CLIENT_ID, CLIENT_SECRET)
#viagem = str(input('Qual ano voce quer viajar? digite a data nesse formato YYYY '))
with open('token.txt', 'r') as file:
    create_playlist(USER_ID, file.read())
