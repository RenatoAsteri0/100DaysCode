from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
import requests

# BS4 ---- ler e extrair o site zillow
ZILLOW_SITE = 'https://appbrewery.github.io/Zillow-Clone/'

zillow_html = requests.get(ZILLOW_SITE)
soup = BeautifulSoup(zillow_html.text, 'html.parser')

# BS4 ---- coletar e agrupar em dicionário o local, endereço e url
precos = soup.find_all('span', class_='PropertyCardWrapper__StyledPriceLine')
preco = [preco.getText() for preco in precos]

enderecos = soup.find_all('a', class_='StyledPropertyCardDataArea-anchor')
endereco = [endereco.getText().strip() for endereco in enderecos]

urls = soup.find_all('a', class_='StyledPropertyCardDataArea-anchor')
url = [url.get('href') for url in urls]

dados = [(p, e, u) for p, e, u in zip(preco, endereco, url)]


# SELENIUM ---- escrever os dados no google forms
FORMS_SITE = ('https://docs.google.com/forms/d/e/1FAIpQLSdqEd6-dPX1sySs8EDe0UGsCe617AryE_2hdKM9cf8tTH555w/viewform?usp='
              'dialog')

options = Options()
options.add_argument('--start-maximized')

driver = webdriver.Chrome(options=options)
for dado in dados:
    driver.get(FORMS_SITE)
    driver.refresh()

    wait = WebDriverWait(driver, 3)
    preco_input = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div'
                                                                       '/div[2]/div/div[1]/div/div[1]/input')))
    preco_input.click()
    preco_input.send_keys(dado[0])
    endereco_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/di'
                                                   'v[1]/div/div[1]/input')
    endereco_input.click()
    endereco_input.send_keys(dado[1])
    url_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/d'
                                              'iv/div[1]/input')
    url_input.click()
    url_input.send_keys(dado[2])

    botao_enviar = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    botao_enviar.click()

