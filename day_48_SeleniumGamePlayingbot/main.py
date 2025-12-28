from selenium import webdriver
from selenium.webdriver.common.by import By

chorme_options = webdriver.ChromeOptions()
driver = webdriver.Chrome()

driver.get('https://www.python.org/')

upcoming_events = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
for time in upcoming_events:
    print(time.text)
driver.quit()