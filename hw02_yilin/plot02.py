import matplotlib.pyplot as plt
import json

with open("/Users/liyilin/Desktop/csci40_work_yilin/hw02_yilin/data/global_temp_anamoly.json") as tempJson:
    # tempData is a dict, key=year, temp=value
    tempData = json.load(tempJson)["data"]

fig, ax = plt.subplots()
xs = []
ys = []
for k, v in tempData.items():
    xs.append(k)
    ys.append(v)
ax.set(
    xlabel='year',
    ylabel='anomolies between ocean and land in Celsius',
)
# print ('xs=', xs)
# print ('ys=', ys)

plt.plot(xs[110:], ys[110:])  # plot(firstINput, secondINput)
plt.xticks(rotation=90)
plt.show()
#print (len(xs))
