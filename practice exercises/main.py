from numpy import average
import pandas as pd
import csv

# with open("weather_data.csv") as weather:
#     weather_data = weather.readlines()
#     print(weather_data)



# with open("weather_data.csv") as weather:
#     weather_data = csv.reader(weather)
#     temps = []

#     for row in weather_data:
#         if row[1] != "temp":
#             temps.append(int(row[1]))
#     print(temps)


data = pd.read_csv("weather_data.csv")

data_dict = data.to_dict()


temps = data["temp"].to_list()

average(temps)
data["temp"].mean()

# Getting the highest temperature
data["temp"].max()


# Getting the rows in the dataframe
print(data[data["day"] == "Monday"])


# Get the day that had the highest temperature
print(data[data["temp"] == data["temp"].max()])


monday = data[data.day == "Monday"]
print(monday.condition)


# Create a dataframe
data_dict = {
    "students":["Amy","Lerato","Celine"],
    "grades": [23,94,68]
}
student_data = pd.DataFrame(data_dict)
print(student_data)

student_data.to_csv("student_grades.csv")

