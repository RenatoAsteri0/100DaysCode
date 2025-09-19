class DataManager:
    #This class is responsible for talking to the Google Sheet.
    pass
import requests
headers = {'Authorization': 'Bearer APIKeySheetFlight'}
response = requests.get('https://api.sheety.co/998db4b1cd9676aab0abe91eb37faacb/flightDeals/prices', headers=headers)
print(response.json())