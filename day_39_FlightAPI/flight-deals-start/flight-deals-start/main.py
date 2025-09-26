#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

# flight_data.py find_cheapest_flight()
# flight_search.py check_flights()

data_manager = DataManager()
sheet_data = data_manager.get_sheed_data()
LOCAL_SAIDA = 'LGW'
flighsearch = FlightSearch()
notification_manager = NotificationManager()
if sheet_data[0]['iataCode'] == '':
    for row in sheet_data:
        row['iataCode'] = flighsearch.get_destination_code(row['city'])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.put_sheet_data()

# ==================== Search for Flights ====================
amanha = datetime.now() + timedelta(days=1)
seis_meses_depois = '2025-12-01'
for destination in sheet_data:
    flight = flighsearch.check_flights(
        LOCAL_SAIDA,
        destination['iataCode'],
        from_data=amanha,
        data_to=seis_meses_depois)
    cheapest_flight = find_cheapest_flight(flight)
    print(f'{destination['city']}: EUR {cheapest_flight.price}')
    sheet_data[0]['lowestPrice'] = float(sheet_data[0]['lowestPrice'])
    cheapest_flight.price = float(cheapest_flight.price)
    if cheapest_flight.price < sheet_data[0]['lowestPrice']:
        notification_manager.notify_chepest_price(cheapest_flight.price, cheapest_flight.origin_ariport,
                                                  cheapest_flight.destination_ariport, cheapest_flight.out_date)
    time.sleep(2)