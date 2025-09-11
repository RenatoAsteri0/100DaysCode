import json
import requests
from twilio.rest import Client



API = 'https://api.openweathermap.org/data/2.5/forecast'
weather_paramters = {
    'lat': -3.75,
    'lon': -73.25,
    'appid': 'eb46f4758dfa42a573030f1488ef4515',
    'cnt': 4,
}
response = requests.get(API, params=weather_paramters)
json_format = response.json()

will_rain = False
for forecast in range(0, len(json_format['list'])):
    id = json_format['list'][forecast]['weather'][0]['id']
    description = json_format['list'][forecast]['weather'][0]['description']
    dia = json_format['list'][forecast]['dt_txt']
    if id < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_= '+19122447476',
        body= 'Leve o guarda chuvas',
        to='+5519996234793'
    )
    print(message.sid)