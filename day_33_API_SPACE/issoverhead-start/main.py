import time
import requests
from datetime import datetime
import smtplib

MY_LAT = -23.037165  # Your latitude
MY_LONG = -47.262246  # Your longitude

def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+ and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now <= sunrise and time_now >= sunset:
        return True

#If the ISS is close to my current position and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

if is_overhead() and is_night():
    while True:
        time.sleep(60)
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_username = 'renato.asterio2@gmail.com'
        smtp_password = 'uuum vetj ikaz vlzs'
        from_addr = 'renato.asterio2@gmail.com'
        to_addr = 'renato.asterio.ext@ultra.com.br'

        with smtplib.SMTP(host=smtp_server, port=smtp_port) as connection:
            connection.starttls()
            connection.login(user=smtp_username, password=smtp_password)
            connection.sendmail(
                to_addrs=to_addr,
                from_addr=from_addr,
                msg="Look Up!"
            )
