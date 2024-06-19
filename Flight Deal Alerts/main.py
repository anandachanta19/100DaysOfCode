from flight_search import FlightSearch
from data_manager import DataManager

flights = FlightSearch()
data_manager = DataManager()
data = dict(data_manager.get_data())
sheet_data = list(data["prices"])

# Add IATA Codes
for city in sheet_data:
    if city["iataCode"] == "":
        data_manager.put_iata(iata=flights.get_iata_code(city["city"]), row_id=city["id"])

