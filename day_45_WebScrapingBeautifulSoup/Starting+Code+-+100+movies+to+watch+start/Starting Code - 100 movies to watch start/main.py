from webbrowser import Chrome
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://www.imdb.com/pt/list/ls599610113/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0'
                         '.3029.110 Safari/537.3'}

# Write your code below this line 👇

service = webdriver.ChromeService()
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get(URL)
response = requests.get(URL, headers=headers)
web_page = response.text
soup = BeautifulSoup(web_page, 'html.parser')

class_filmes = soup.find_all(class_="ipc-title-link-wrapper")
print(len(class_filmes))
for filme in class_filmes:
    print(filme)
    with open('melhores_filmes.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{filme.getText()}\n')