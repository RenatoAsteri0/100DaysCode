from bs4 import BeautifulSoup
import requests

# Using what you've learnt about BeautifulSoup, scrape the top 100 song titles on that date into a Python List

viagem = str(input('Qual ano voce quer viajar? digite a data nesse formato YYYY '))

url = 'https://playback.fm/charts/top-100-songs/' + viagem
response = requests.get(url)
web_page = response.text
soup = BeautifulSoup(web_page, 'html.parser')

find_name = soup.find_all(class_='song', itemprop="name")
find_position = soup.find_all('td')
name = [song.getText() for song in find_name]
position = [pos.getText(strip=True) for pos in find_position if pos.getText(strip=True).isdigit()]

songs = {n: p for n, p in zip(name, position)}
print(songs)