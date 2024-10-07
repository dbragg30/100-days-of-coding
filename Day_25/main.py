import csv
import pandas


# with open('weather_data.csv', newline="") as csvfile:
#     csvfile = csvfile.readlines()
#     data = list(csvfile)
#     print(data)

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     #print(temperatures)
#
# col_names = ['Day', 'Temp', 'Condition']
#data = pandas.read_csv('weather_data.csv')
# #print(data["temp"])
# data_dict = data.to_dict()
# #print(data_dict)
#
# temp_list = data["temp"].to_list()
# average = sum(temp_list) / len(temp_list)
# print(average)
# TA = pandas.DataFrame(temp_list)
# print(TA.mean())
#
# print(data["temp"].mean())
#
# print(data["temp"].max())

# get data in Row
# print(data[data.day == "Monday"])
# #max_temp = data['temp'].max()
# print(data[data['temp'] == data['temp'].max()])
# monday = data[data.day == "Monday"]
# print((monday.temp * 9/5) + 32)

# create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "Jame", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240124.csv')
fur = "Primary Fur Color"
# gray_count = data[fur].value_counts()['Gray']
# red_count = int(data[fur].value_counts()['Cinnamon'])
# black_count = int(data[fur].value_counts()['Black'])
# print(gray_count)
# print(red_count)
# print(black_count)
#
# data_dict = {
#     "Gray": [gray_count],
#     "Red": [red_count],
#     "Black": [black_count]
# }
# print(data_dict)
# data1 = pandas.DataFrame(data_dict)
# data1.to_csv("Squirrel_Count.csv")


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240124.csv")
grey_sl = len(data[data[fur] == "Gray"])
red_sl = len(data[data[fur] == "Cinnamon"])
black_sl = len(data[data[fur] == "Black"])
print(grey_sl)
print(red_sl)
print(black_sl)

data_dict= {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "count": [grey_sl, red_sl, black_sl]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_Count.csv")