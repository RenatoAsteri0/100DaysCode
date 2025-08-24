##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name
# from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
import datetime as dt
import random
import smtplib

def check_birthday():
    data = pd.read_csv('birthdays.csv')
    dataframe = pd.DataFrame(data)
    renato_row = dataframe.loc[dataframe['name'] == 'renato']
    print(type(f"aniversario: {renato_row.month}/{renato_row.day}"))

    hoje = dt.date.today()
    return (hoje.month, hoje.day) == (int(renato_row['month'].iloc[0]), int(renato_row['day'].iloc[0]))

def retruscture_letter():
    random_letter = random.randint(1,3)
    with open(f'letter_templates/letter_{random_letter}.txt') as file:
        content = file.read().replace('[NAME]', 'Renato')
        return content

def send_email(message):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'renato.asterio2@gmail.com'
    smtp_password = 'uuum vetj ikaz vlzs'
    from_addr = 'renato.asterio2@gmail.com'
    to_addr = 'renato.asterio.ext@ultra.com.br'
    print(message)
    with smtplib.SMTP(host=smtp_server, port=smtp_port) as connection:
        connection.starttls()
        connection.login(user=smtp_username, password=smtp_password)
        connection.sendmail(
            from_addr=from_addr,
            to_addrs=to_addr,
            msg=(message)
        )

def main():
    if check_birthday():
        retruscture_letter()
        send_email(retruscture_letter())
        print('email enviado')

main()