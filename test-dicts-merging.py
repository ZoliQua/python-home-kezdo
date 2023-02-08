# Python Test Project File
# Written by Zoltan Dul (2021)
#

# SORUCE: https://medium.com/techtofreedom/7-ways-to-merge-dictionaries-in-python-6d6e6f191ae8

# Merging brute force

cities_1 = {'New York City': 'US', 'Los Angeles': 'US'}
cities_2 = {'London': 'UK', 'Birmingham': 'UK'}

cities_1['London'] = 'UK'
cities_1['Birmingham'] = 'UK'
print(cities_1)

# Using update function

cities_1 = {'New York City': 'US', 'Los Angeles': 'US'}
cities_2 = {'London': 'UK', 'Birmingham': 'UK'}

cities_1.update(cities_2)
print(cities_1)

# Unpack and merge two dicts

cities_1 = {'New York City': 'US', 'Los Angeles': 'US'}
cities_2 = {'London': 'UK', 'Birmingham': 'UK'}

cities = {**cities_1, **cities_2}
print(cities)

# Use dict comprehension

cities_us = {'New York City': 'US', 'Los Angeles': 'US'}
cities_uk = {'London': 'UK', 'Birmingham': 'UK'}

cities = {k: v for d in [cities_us, cities_uk] for k, v in d.items()}
print(cities)

# Using union operator from Python 3.9

cities_us = {'New York City': 'US', 'Los Angeles': 'US'}
cities_uk = {'London': 'UK', 'Birmingham': 'UK'}

# cities = cities_us|cities_uk
# print(cities)

# Using ChainMap

from collections import ChainMap

cities_us = {'New York City': 'US', 'Los Angeles': 'US'}
cities_uk = {'London': 'UK', 'Birmingham': 'UK'}

cities = dict(ChainMap(cities_us, cities_uk))
print(cities)

# Using chainmap - itertools

from itertools import chain

cities_us = {'New York City': 'US', 'Los Angeles': 'US'}
cities_uk = {'London': 'UK', 'Birmingham': 'UK'}

cities = dict(chain(cities_us.items(), cities_uk.items()))
print(cities)