# import csv
#
# # Storing Temperatures
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     flag = True
#     for row in data:
#         if flag:
#             flag = False
#             continue
#         temperature = int(row[1])
#         temperatures.append(temperature)
#
# print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(f"Average Temperature: {data["temp"].mean()}")
print(f"Maximum Temperature: {data["temp"].max()}")
