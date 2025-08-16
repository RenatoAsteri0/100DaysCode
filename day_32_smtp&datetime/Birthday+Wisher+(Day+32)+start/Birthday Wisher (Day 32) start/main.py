import random
import smtplib
import datetime as dt

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'renato.asterio2@gmail.com'
smtp_password = 'uuum vetj ikaz vlzs'
from_addr = 'renato.asterio2@gmail.com'
to_addr = 'renato.asterio.ext@ultra.com.br'
subject = 'Teste'
body = 'Ola'

hoje = str(dt.date.today())

def generate_random_phase():
    with open('quotes.txt', 'r') as file:
        readed_file = file.readlines()
        random_phase = random.choices(readed_file)[0]
        return random_phase

def enviar_aniver_email(motivation):
    with smtplib.SMTP('smtp.gmail.com', port=smtp_port) as connection:
        connection.starttls()
        connection.login(user=smtp_username, password=smtp_password)
        connection.sendmail(
            from_addr=from_addr,
            to_addrs=to_addr,
            msg=(motivation)
        )


def main():
    if hoje == "2025-08-16":
        print('ola')
        frase = generate_random_phase()
        print(frase)
        enviar_aniver_email(frase)

main()