# import pytest
# import os
#
# from population_data import calc_population_change
#
# @pytest.fixture
# def population_file(tmp_path):
#     # Create a temporary file with population data
#     file_path = tmp_path / "population_data.txt"
#     with open(file_path, "w") as f:
#         f.write("United States, 2010, 308745538\n")
#         f.write("United States, 2011, 311591917\n")
#         f.write("United States, 2012, 314311158\n")
#         f.write("China, 2010, 1337705000\n")
#         f.write("China, 2011, 1343239923\n")
#         f.write("China, 2012, 1349585838\n")
#         f.write("India, 2010, 1210193422\n")
#         f.write("India, 2011, 1220845451\n")
#         f.write("India, 2012, 1230980691\n")
#     yield file_path
#     # Clean up the temporary file
#     os.remove(file_path)
#
# def test_calc_population_change(population_file):
#     # Test the calc_population_change function
#     expected_data = {
#         "United States": {2010: 0, 2011: 2849379, 2012: 2717241},
#         "China": {2010: 0, 2011: 5534923, 2012: 6345915},
#         "India": {2010: 0, 2011: 10622029, 2012: 10175240},
#     }
#     assert calc_population_change(population_file) == expected_data
#
# @pytest.mark.parametrize("filename, expected", [
#     ("population_data.txt", {
#         "United States": {2010: 0, 2011: 2849379, 2012: 2717241},
#         "China": {2010: 0, 2011: 5534923, 2012: 6345915},
#         "India": {2010: 0, 2011: 10622029, 2012: 10175240},
#     }),
#     ("empty_file.txt", {}),
# ])
# def test_calc_population_change_parametrize(filename, expected, tmp_path):
#     # Test the calc_population_change function with parametrization
#     file_path = tmp_path / filename
#     with open(file_path, "w") as f:
#         pass  # Create an empty file
#     assert calc_population_change(file_path) == expected

# import pytest
# import os
#
# from my_module import calc_population_change
#
# @pytest.fixture
# def temp_file():
#     data = [
#         "USA, 2019, 329064917\n",
#         "USA, 2020, 331002651\n",
#         "China, 2019, 1439323776\n",
#         "China, 2020, 1444216107\n",
#         "India, 2019, 1366417756\n",
#         "India, 2020, 1380004385\n",
#     ]
#     filename = "temp_population_data.txt"
#     with open(filename, "w") as f:
#         f.writelines(data)
#     yield filename
#     os.remove(filename)
#
# def test_calc_population_change(temp_file):
#     expected_data = {
#         "USA": {2020: 1938734, "last_population": 329064917, "last_year": 2019},
#         "China": {2020: 4892331, "last_population": 1439323776, "last_year": 2019},
#         "India": {2020: 13506629, "last_population": 1366417756, "last_year": 2019},
#     }
#     assert calc_population_change(temp_file) == expected_data
#
# def test_calc_population_change_file_not_exist():
#     with pytest.raises(FileNotFoundError):
#         calc_population_change("non_existing_file.txt")

# import pytest
# import os
#
# from population_change import calc_population_change
# # from main import calc_population_change
#
# @pytest.fixture
# def population_data_file(tmp_path):
#     file_path = tmp_path / "population_data.txt"
#     with open(file_path, "w") as f:
#         f.write("USA, 2000, 280000000\n")
#         f.write("USA, 2001, 282000000\n")
#         f.write("USA, 2002, 284000000\n")
#         f.write("Canada, 2000, 31000000\n")
#         f.write("Canada, 2001, 31300000\n")
#         f.write("Canada, 2002, 31600000\n")
#     yield str(file_path)
#
#
# def test_calc_population_change(population_data_file):
#     expected_data = {
#         "USA": {
#             2000: None,
#             2001: 2000000,
#             2002: 2000000,
#         },
#         "Canada": {
#             2000: None,
#             2001: 300000,
#             2002: 300000,
#         },
#     }
#     assert calc_population_change(population_data_file) == expected_data
#
#
# def test_calc_population_change_empty_file(tmp_path):
#     empty_file = tmp_path / "empty.txt"
#     empty_file.write("")
#     with pytest.raises(ValueError):
#         calc_population_change(str(empty_file))
#
#
# def test_calc_population_change_missing_file():
#     with pytest.raises(FileNotFoundError):
#         calc_population_change("non_existing_file.txt")

# import os
# import pytest
#
# from main import calc_population_change
#
# @pytest.fixture
# def population_data_file(tmpdir):
#     file_content = [
#         'USA, 2020, 328000000\n',
#         'USA, 2021, 330000000\n',
#         'China, 2020, 1400000000\n',
#         'China, 2021, 1410000000\n',
#         'India, 2020, 1360000000\n',
#         'India, 2021, 1370000000\n',
#     ]
#     file_path = tmpdir.join('population_data.txt')
#     with open(file_path, 'w') as f:
#         f.writelines(file_content)
#     return str(file_path)
#
#
# def test_calc_population_change_with_valid_file(population_data_file):
#     expected_data = {
#         'USA': {2020: 328000000, 2021: 2000000},
#         'China': {2020: 1400000000, 2021: 10000000},
#         'India': {2020: 1360000000, 2021: 10000000},
#     }
#     assert calc_population_change(population_data_file) == expected_data
#
#
# def test_calc_population_change_with_invalid_file():
#     with pytest.raises(FileNotFoundError):
#         calc_population_change('invalid_file.txt')
#
#
# @pytest.mark.parametrize('input_file_content, expected_data', [
#     ([
#         'USA, 2020, 328000000\n',
#         'USA, 2021, 330000000\n',
#     ], {
#         'USA': {2020: 328000000, 2021: 2000000},
#     }),
#     ([
#         'China, 2020, 1400000000\n',
#         'China, 2021, 1410000000\n',
#     ], {
#         'China': {2020: 1400000000, 2021: 10000000},
#     }),
#     ([
#         'India, 2020, 1360000000\n',
#         'India, 2021, 1370000000\n',
#     ], {
#         'India': {2020: 1360000000, 2021: 10000000},
#     }),
# ])
# def test_calc_population_change_with_parametrization(input_file_content, expected_data, tmpdir):
#     file_path = tmpdir.join('population_data.txt')
#     with open(file_path, 'w') as f:
#         f.writelines(input_file_content)
#     assert calc_population_change(str(file_path)) == expected_data

# import os
# import pytest
#
# @pytest.fixture
# def population_data():
#
#
#     return "test_data.txt"
#
#
# # def test_calc_population_change(population_data):
# #     from main import calc_population_change
# #
# #     expected_result = {
# #         'United States': {2011: 2848379, 2012: 2714241},
# #         'China': {2011: 5534923, 2012: 6345915},
# #         'India': {2011: 10622029, 2012: 10135240}
# #     }
# #     result = calc_population_change(population_data)
# #     assert result == expected_result
#
# @pytest.mark.parametrize("country, year, population, expected_result", [
#     ("United States", 2011, 311591917, 2848379),
#     ("China", 2012, 1349585838, 6345915),
#     ("India", 2011, 1220845451, 10622029),
# ])
# def test_calc_population_change_single(population_data, country, year, population, expected_result):
#     from main import calc_population_change
#
#     with open(population_data, 'a') as f:
#         f.write(f"{country}, {year}, {population}\n")
#
#     result = calc_population_change(population_data)
#     assert result[country][year] == expected_result

import pytest
import os

@pytest.fixture(scope="module")
def population_data():
    file_path = "../population_data.txt"
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
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
    else:
        pytest.skip("File does not exist.")
@pytest.mark.parametrize("country, year, expected_result", [
    ("United States", 2011, {2010: 0, 2011: 2848379}),
    ("United States", 2012, {2011: 2250279, 2012: 2711241}),
    ("China", 2011, {2010: 0, 2011: 5533923}),
    ("China", 2012, {2011: 5533923, 2012: 5534294})
])
def test_calc_population_change(population_data, country, year, expected_result):
    assert population_data[country][year] == expected_result



