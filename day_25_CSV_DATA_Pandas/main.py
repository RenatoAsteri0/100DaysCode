'''with open('weather_data.csv', mode='r') as data:
    data_file = data.readlines()
print(data_file)'''

'''import csv

with open('weather_data.csv') as data_file:
    data = csv.reader(data_file)
    temp = []
    for row in data:
        celula_temp = row[1]
        if celula_temp != 'temp':
            num_int = temp.append(int(celula_temp))
print(temp)

import pandas as pd
import statistics

data = pd.read_csv('weather_data.csv')
#print(data['temp'])
data_temp = data['temp'].to_list()
temp_avg = data['temp'].mean()
temp_max = data['temp'].max()
print(data_temp)
print(temp_avg)
print(temp_max)
print('\n')
print(data[data.temp == data['temp'].max()])
monday = data[data.day == 'Monday']
# fahrenheit = (celsius * 9/5) + 32
monday_temp = monday.temp[0]
monday_fare = (monday_temp * 9/5) + 32
print(monday_fare)'''

import pandas as pd

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
colors_data = data['Primary Fur Color'].value_counts(dropna=False)
colors_data.to_csv('squirrel_count.csv1')
with open('squirrel_count.csv', 'w') as file:
    file.write(str(colors_data))
