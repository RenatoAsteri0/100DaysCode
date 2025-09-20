#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
import pprint

data_manager = DataManager()
sheet_data = data_manager.get_sheed_data()
print(sheet_data)

if sheet_data[0]['iataCode'] == '':
    flighsearch = FlightSearch()
    for row in sheet_data:
        row['iataCode'] = flighsearch.get_destination_code(row['city'])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.put_sheet_data()
