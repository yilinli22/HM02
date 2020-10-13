import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('data/countries.csv')
japan = data[data.country == 'Japan']
china = data[data.country == 'China']

plt.plot(japan.year, japan.population / 10**6)
plt.plot(china.year, china.population / 10**6)
plt.title('Population Growth Over the Years: China vs. Japan')
plt.legend(['Japan', 'China'])
plt.xlabel('Year')
plt.ylabel('Population (in millions)')
plt.show()
