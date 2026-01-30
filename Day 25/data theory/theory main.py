# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
#
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperature = int(row[1])
#             temperatures.append(temperature)
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)
#
# print(data["temp"].mean()) # average temperature
#
# print(data["temp"].max())

# Get Data in Row
# print(data[data.temp == data.temp.max()]) # Getting maximum temperature Day

# Get the particular condition of the particular day
monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
fahrenheit_monday = monday_temp*1.8+32
print(fahrenheit_monday)

# # Create dataframe from scratch
# data_dict = {
#     "students":["Amy","James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv", index = False) # index is True by default




# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# gray_sq_count = len(data[data["Primary Fur Color"] == "Gray"]) # len() counts the number of lines with Gray color
# red_sq_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_sq_count = len(data[data["Primary Fur Color"] == "Black"])
# print(gray_sq_count)
# print(red_sq_count)
# print(black_sq_count)
#
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [gray_sq_count, red_sq_count,black_sq_count]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("squirrel_count.csv", index = False)