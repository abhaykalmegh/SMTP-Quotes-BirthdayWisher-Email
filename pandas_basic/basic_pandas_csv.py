
# Note:- Try this one by one

#### File opening using file handaling methods ####

with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)


#### File opening using CSV module ####

import csv
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperature = []
    for row in data:
        if row[1] != "temp":
            temperature.append(int(row[1]))
    print(temperature)

####  File opening using Pandas module ####
import pandas
import pprint

data = pandas.read_csv("weather_data.csv")
print(data)
# print(type(data))
# print(type(data['temp']))
# data_dict = data.to_dict()
# pprint.pprint(data_dict)

temp_list = data["temp"].to_list
# print(temp_list)
# print(data["temp"].mean())
# print(data["temp"].max())

#### get dta from coloum ####

# print(data["condition"])
# print(data.condition)

#### get data from row ####
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

m_temp = monday.temp



# create data_frame from scratch (conversion dict to csv)

data_dict = {
      "students": ["Abhay", "Ramji", "Sitamata"],
      "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")