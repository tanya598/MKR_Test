import os


def calc_population_change(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        data = {}

