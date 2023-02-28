import random
print('random => ', random.random())

import pandas
house = pandas.read_csv('house.csv')
print(house)
print(house.max())
print(house.min())
print(house.describe())