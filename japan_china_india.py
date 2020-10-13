import pandas as pd
from matplotlib import pyplot as plt
import plotly.express as px
# import data and create lists of x-variable
data = pd.read_csv('data/countries.csv')
japan = data[data.country == 'Japan']
china = data[data.country == 'China']
india = data[data.country == 'India']
# print ('japan=', japan)
# print(japan.year)
# print(data[data.country=='Japan'][3])
# years = data['year']
# print(data.year)
# print (japan)
# print (china)
# print (india)
# name x axis and y axis
fig, ax = plt.subplots()
ax.set(
    xlabel='year',
    ylabel='Population (in billions)',
    title='Population Growth: China vs. Japan vs. India'
)

#fig = px.line(data, x = 'year', y = 'Population (in billions)', title='Population Growth From 1950: China vs. Japan vs. India')

# plt.title('Population Growth From 1950: China vs. Japan vs. India')

plt.legend(['Japan', 'China', 'India'])
plt.plot(japan.year, japan.population / 10**9, 'bo')
plt.plot(china.year, china.population / 10**9, 'r+')
plt.plot(india.year, india.population / 10**9, 'g*')
plt.show()
