import os


def calc_population_change(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        data = {}

        for line in lines:
            country, year, population = line.strip().split(', ')
            year, population = int(year), int(population)
            if country not in data: