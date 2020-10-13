import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('data/countries.csv')
japan = data[data.country == 'Japan']
china = data[data.country == 'China']
india = data[data.country == 'India']

plt.plot(japan.year, japan.population / 10**6)
plt.plot(china.year, china.population / 10**6)
plt.plot(india.year, india.population / 10**6)
plt.title('Population Growth Over the Years: China vs. Japan vs. India')
plt.legend(['Japan', 'China', 'India'])
plt.xlabel('Year')
plt.ylabel('Population (in millions)')
plt.show()
