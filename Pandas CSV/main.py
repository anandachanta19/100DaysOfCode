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

#
# data = pandas.read_csv("weather_data.csv")
# print(f"Average Temperature: {data["temp"].mean()}")
# print(f"Maximum Temperature: {data["temp"].max()}")
#
# print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# print(f"{(monday["temp"] * 9/5) + 32}")


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# Converting Fur color data to list
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Squirrel count": [gray_count, cinnamon_count, black_count]
}

color_data = pandas.DataFrame(data_dict)
color_data.to_csv("Squirrel_color_data.csv")
