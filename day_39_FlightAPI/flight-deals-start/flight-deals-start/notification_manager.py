from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()
class NotificationManager(Client):
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        super().__init__(
            os.environ['Account_sid_twillio'],
            os.environ['Auth_token_twillio']
        )

    def notify_chepest_price(self, price, local_saida, local_destino, data_saida):
        response = self.messages.create(
            from_= '+19122447476',
            body= f'Low price Alert! Only EUR{price} to fly from {local_saida} to {local_destino} no dia {data_saida}',
            to='+5519996234793'
        )
        print(response.sid)
