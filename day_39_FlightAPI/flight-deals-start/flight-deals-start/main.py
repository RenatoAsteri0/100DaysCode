#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from datetime import datetime, timedelta

# flight_data.py find_cheapest_flight()
# flight_search.py check_flights()

data_manager = DataManager()
sheet_data = data_manager.get_sheed_data()
LOCAL_SAIDA = 'LON'

if sheet_data[0]['iataCode'] == '':
    flighsearch = FlightSearch()
    for row in sheet_data:
        row['iataCode'] = flighsearch.get_destination_code(row['city'])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.put_sheet_data()

# ==================== Search for Flights ====================
amanha = datetime.now() + timedelta(days=1)
seis_meses_depois = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flighsearch.check_flights(
        LOCAL_SAIDA,
        destination['iataCode'],
        date_from=amanha,
        date_to=seis_meses_depois)
    cheapest_flight = find_cheapeast_flight(flight)