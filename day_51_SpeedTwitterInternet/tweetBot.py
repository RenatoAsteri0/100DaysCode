from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.down = 0
        self.up = 0
        self.wait = WebDriverWait(self.driver, 30)


    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/pt')
        button_iniciar = self.wait.until(ec.presence_of_element_located((By.CLASS_NAME, "start-text")))
        button_iniciar.click()
        info_down =  self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'span.download-speed')))
        self.down = info_down.text
        info_up = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'span.upload-speed')))
        self.up = info_up.text

        print(f'down: {self.down}\nup: {self.up}')


    def tweet_at_provider(self):
        pass
