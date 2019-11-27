import pandas as pd

from matplotlib import pyplot as plt

x = [1, 2, 3]
y = [1, 4, 9]
z = [10, 5, 0]
# plt.plot(x, y)
# plt.plot(x, z)
# plt.title("test plot")
# plt.xlabel("x")
# plt.ylabel("y and z")
# plt.legend(["this is y", "this is z"])
# sample_data = pd.read_csv('sample_data.csv')
# print(sample_data)
# print(type(sample_data))
# print(sample_data.column_c)
# print(type(sample_data.column_c))
# print(sample_data.column_c.iloc[2])
# plt.show()

# plt.plot(sample_data.column_a, sample_data.column_b, '.')
# plt.plot(sample_data.column_a, sample_data.column_c)
# plt.show()

data = pd.read_csv('countries.csv')
# print(data)
# print(data.country == 'United States')
us = data[data.country == 'United States']
# print(us)
china = data[data.country == 'China']
print(china)
plt.plot(us.year, us.population * 100/ us.population.iloc[0])
plt.plot(china.year, china.population * 100/ china.population.iloc[0])
plt.xlabel("Year")
plt.ylabel("Population percent growth since 1952")
plt.legend(["US", "China"])
plt.show()