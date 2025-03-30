import json


with open('Data.json', 'r') as file:
    data = json.load(file)

gdp_data = data[1]


for entry in gdp_data:
    date = entry.get('date')  
    value = entry.get('value') 
    print(f"Year: {date}, GDP: {value}")