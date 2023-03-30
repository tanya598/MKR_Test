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
