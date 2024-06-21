from datetime import datetime as dt, timedelta

import flight_search

from_time = dt.now().date().strftime("%Y-%m-%d")
to_time = (dt.now() + timedelta(days=(6 * 30))).date().strftime("%Y-%m-%d")


class FlightData:
    def __init__(self):
        self.price = None
        self.origin_airport = None
        self.destination_airport = None
        self.out_date = None
        self.stops = None
        self.return_date = None

    def get_data(self, flight_details: flight_search, origin_city, destination):
        print(f"Getting flights for {destination["city"]}...")
        flights = flight_details.check_flights(
            origin_city,
            destination["iataCode"],
            from_time,
            to_time
        )
        for flight in flights["data"]:
            self.price = flight["price"]["total"]
            self.origin_airport = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            self.destination_airport = \
                flight["itineraries"][0]["segments"][len(flight["itineraries"][0]["segments"]) - 1]["arrival"][
                    "iataCode"]
            self.out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            self.return_date = \
                flight["itineraries"][0]["segments"][len(flight["itineraries"][0]["segments"]) - 1]["arrival"][
                    "at"].split("T")[0]
            self.stops = len(flight["itineraries"][0]["segments"])
