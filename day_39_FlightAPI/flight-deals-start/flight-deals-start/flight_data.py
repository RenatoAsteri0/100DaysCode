class FlightData:

    def __init__(self, price, origin_ariport, destination_ariport, out_date, return_date):
        self.price = price
        self.origin_ariport = origin_ariport
        self.destination_ariport = destination_ariport
        self.out_date = out_date
        self.return_date = return_date

def find_cheapest_flight(data):
    if data is None:
        print('sem resultados')
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

    primeiro_voo = data['data'][0]
    preco_mais_barato = primeiro_voo['price']['grandTotal']
    local_saida = primeiro_voo['itineraries'][0]['segments'][0]['departure']['iataCode']
    local_chegada = primeiro_voo['itineraries'][0]['segments'][0]['arrival']['iataCode']
    dia_saida = primeiro_voo['itineraries'][0]['segments'][0]['departure']['at'].split('T')[0]
    dia_chegada = primeiro_voo['itineraries'][0]['segments'][0]['arrival']['at'].split('T')[0]

    chepest_flight = FlightData(price=preco_mais_barato, origin_ariport=local_saida, destination_ariport=local_chegada,
                                out_date=dia_saida, return_date=dia_chegada)

    for flight in data['data']:
        price = float(flight['price']['grandTotal'])
        preco_mais_barato = float(preco_mais_barato)
        if price < preco_mais_barato:
            local_saida = primeiro_voo['itineraries'][0]['segments'][0]['departure']['iataCode']
            local_chegada = primeiro_voo['itineraries'][0]['segments'][0]['arrival']['iataCode']
            dia_saida = primeiro_voo['itineraries'][0]['segments'][0]['departure']['at'].split('T')[0]
            dia_chegada = primeiro_voo['itineraries'][0]['segments'][0]['arrival']['at'].split('T')[0]
            chepest_flight = FlightData(price=preco_mais_barato, origin_ariport=local_saida,
                                        destination_ariport=local_chegada,
                                        out_date=dia_saida, return_date=dia_chegada)
    return chepest_flight
