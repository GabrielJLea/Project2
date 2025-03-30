import json

# Load the JSON data from the file
with open('Data.json', 'r') as file:
    data = json.load(file)

gdp_data = data[1]

# Loop through the list and print out relevant information
for entry in gdp_data:
    date = entry.get('date')  # Get the date
    value = entry.get('value')  # Get the GDP value
    print(f"Year: {date}, GDP: {value}")