from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.get('https://en.wikipedia.org/wiki/Main_Page')


qnts_articles = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
print(qnts_articles.text)
driver.quit()