from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os

ACCOUNT_EMAIL = "angela@test.com"  # The email you registered with
ACCOUNT_PASSWORD = "superSecretTestPassword"      # The password you used during registration
GYM_URL = "https://appbrewery.github.io/gym/"

chrome_driver = webdriver.ChromeOptions()
chrome_driver.add_argument('--password-store=basic')
chrome_driver.add_experimental_option('detach', True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_driver.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_driver)
driver.get(GYM_URL)


wait = WebDriverWait(driver, 10)
#login
login_button = wait.until(ec.element_to_be_clickable((By.ID, 'login-button')))
login_button.click()

#email e senha
email = wait.until(ec.presence_of_element_located((By.ID, 'email-input')))
email.send_keys(ACCOUNT_EMAIL)
senha = wait.until(ec.presence_of_element_located((By.ID, 'password-input')))
senha.send_keys(ACCOUNT_PASSWORD)

#acessar
submit_button = wait.until(ec.element_to_be_clickable((By.ID, 'submit-button')))
submit_button.click()

#checar se foi sucesso o login
schedule_button = wait.until(ec.element_to_be_clickable((By.ID, 'schedule-link')))
if schedule_button:
    print('login com sucesso')
else:
    print('falha')

#agendar atividade na proxima tuesday
next_tuesday = wait.until(ec.presence_of_element_located((By.XPATH, "//*[starts-with(@id, 'day-group-tue,')]")))
print(next_tuesday.text)
book_class = wait.until(ec.element_to_be_clickable((By.XPATH, "//*[starts-with(@id, 'book-button)]")))
book_class.click()
print('✓ Booked')