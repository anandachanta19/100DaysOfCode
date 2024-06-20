import os
import time
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from twilio.rest import Client

ORIGIN_CITY_CODE = "DEL"

flight_search = FlightSearch()
data_manager = DataManager()
data = dict(data_manager.get_data())
sheet_data = list(data["prices"])

# Add IATA Codes
for destination in sheet_data:
    if destination["iataCode"] == "":
        data_manager.put_iata(iata=flight_search.get_iata_code(destination["city"]), row_id=destination["id"])
        time.sleep(2)

for destination in sheet_data:
    # Populate Flight Data
    flight_info = FlightData()
    flight_info.get_data(
        flight_details=flight_search,
        origin_city=ORIGIN_CITY_CODE,
        destination=destination
    )
    if flight_info.price is not None and float(flight_info.price) <= float(destination["lowestPrice"]):
        print(f"Price to {flight_info.destination_airport} is {flight_info.price}")
        # Send Message Through Twilio
        account_sid = os.getenv("TWILIO_SID")
        auth_token = os.getenv("TWILIO_TOKEN")
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(body=f"Low Price Alert! Only ₹{flight_info.price} to fly from {flight_info.origin_airport}"
                         f" to {flight_info.destination_airport}, on {flight_info.out_date} "
                         f"until {flight_info.return_date}",
                    from_=os.getenv("TWILIO_PHONE_NUMBER"),
                    to=os.getenv("MY_PHONE_NUMBER"))
        print(message.status)
        print(message.sid)
    else:
        print(f"No flights available to {destination["city"]}")
        continue
