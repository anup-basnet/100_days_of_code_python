"""File handling can be annoying to work with lines having white spaces or new lines"""
# with open("./weather-data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)


# import csv

# with open("./weather-data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     print(data)
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


## Pandas Basics
import pandas as pd

data = pd.read_csv("weather-data.csv")
# print(data)
temp_list = data["temp"].to_list()
avg = sum(temp_list) / len(temp_list)
print(avg)
print(data["temp"].max())
print(data[data.temp == data.temp.max()])


monday = data[data.day == "Monday"]
print(monday.condition)
print(monday.temp)
print(f"{int(monday.temp)} deg C to deg F is {int(monday.temp) * 1.8 + 32}")


# Create a dataframe from scratch
data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}
student_data = pd.DataFrame(data_dict)
print(student_data)
student_data.to_csv("new_file.csv")
