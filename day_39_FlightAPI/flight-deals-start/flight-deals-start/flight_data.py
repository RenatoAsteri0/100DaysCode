class FlightData:

    def __init__(self, price, origin_ariport, destination_ariport, out_date, return_date):
        self.price = price
        self.origin_ariport = origin_ariport
        self.destination_ariport = destination_ariport
        self.out_date = out_date
        self.return_date = return_date

    def find_cheapeast_flight(data):