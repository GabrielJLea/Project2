import csv
from collections import defaultdict

homicide_data = defaultdict(lambda: defaultdict(list))

with open('Homicides.csv', mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if len(row) < 6:
            continue
        region = row[1].strip()
        year = row[2].strip()
        series = row[3].strip()
        value = row[4].strip()
        if 'Intentional homicide rates per 100,000' in series:
            homicide_data[year][region].append(value)

for year, regions in homicide_data.items():
    print(f'Year: {year}')
    for region, rates in regions.items():
        print(f'  Region: {region}, Homicide Rates: {", ".join(rates)}')


















