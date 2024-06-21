import os
import time
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager

ORIGIN_CITY_CODE = "VTZ"

flight_search = FlightSearch()
data_manager = DataManager()
data = dict(data_manager.get_data())
sheet_data = list(data["prices"])
notifications = NotificationManager()

# Add IATA Codes
for destination in sheet_data:
    if destination["iataCode"] == "":
        data_manager.put_iata(iata=flight_search.get_iata_code(destination["city"]), row_id=destination["id"])
        time.sleep(2)

# for destination in sheet_data:
#     # Populate Flight Data
#     flight_info = FlightData()
#     flight_info.get_data(
#         flight_details=flight_search,
#         origin_city=ORIGIN_CITY_CODE,
#         destination=destination
#     )
#     if flight_info.price is not None and float(flight_info.price) <= float(destination["lowestPrice"]):
#         print(f"Price to {flight_info.destination_airport} is {flight_info.price}")
#         # Send Message Through Twilio
#         notifications.send_message(flight_info)
#     else:
#         print(f"No flights available to {destination["city"]}")
#         continue


users_data = data_manager.get_customers_emails()["users"]
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
        # Send emails to users
        for user in users_data:
            notifications.send_emails(to=user["what'sYourEmail"], flight_info=flight_info)
    else:
        print(f"No flights available to {destination["city"]}")
        continue
