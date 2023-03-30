import os

def calc_population_change(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        data = {}

        for line in lines:
            country, year, population = line.strip().split(', ')
            year, population = int(year), int(population)
            if country not in data:
                data[country] = {}
            if 'last_year' in data[country]:
                population_change = population - data[country]['last_population']
                data[country][year] = population_change
            data[country]['last_population'] = population
            data[country]['last_year'] = year
        return data


file_path = "population_data.txt"
if os.path.exists(file_path):
    population_change_data = calc_population_change(file_path)
    print(population_change_data)
else:
    print("File does not exist.")