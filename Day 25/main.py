# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
import pandas
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)


# data = pd.read_csv('weather_data.csv')
# print(data['temp'])
# #average
# average_data = data['temp'].sum() / len(data['temp'])
# print(average_data)
# #average with mean()
# average = data['temp'].mean()
# print(average)
#
# print(data['condition'])
# #Get data in row
# print(data[data.day == "Monday"])
#
# print(data[data.temp == data.temp.max()])

# monday = data[data.temp == 24]
# print(f'{monday.day},\n{monday.temp}')
# ((9*c)/5)+32
# print(data['temp'] == )

#Convert celcius to Farenheit
# for temp in data['temp']:
#     F = (9/5)*temp+32
#     F == data['temp']
#     print(F)

#Create a dataframe from scatch
# data_dict = {
#     "students": ["Amy","James","Angela"],
#     "scores": [76,56,65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# # print(data)
import pandas as pd
import csv
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data['Primary Fur Color'] == "Gray"])
red_squirrels_count = len(data[data['Primary Fur Color'] == "Cinnamon"])
black_squirrels_count = len(data[data['Primary Fur Color'] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Grey","Cinnamon","Black"],
    "Count": [grey_squirrels_count,red_squirrels_count,black_squirrels_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

