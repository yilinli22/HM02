import matplotlib.pyplot as plt
import json

with open("/Users/liyilin/Desktop/csci40_work_yilin/hw02_yilin/data/nobel_prize_country.json") as prizeJson:
    prizeData = json.load(prizeJson)["countries"] # this is a list

#print (prizeData)
country_codes =[]
#print(len(prizeData))
for i in range(len(prizeData)):
    if "code" in prizeData[i]:
        country_codes.append(prizeData[i]['code'])
        #print ('prize data first country =', prizeData[i]['code'])
    else:
        pass
print ('country_codes=', country_codes)




new_dict = {}
for i in range(len(prizeData)):
    if "code" in prizeData[i]:
        if prizeData[i]['code'] not in new_dict:
            new_dict[prizeData[i]['code']] = 1
        else: 
            new_dict[prizeData[i]['code']] += 1 # = new_dict['DZ'] = new_dict['DZ'] + 1

    # If the computer doesn't see 'DZ' key in country_codes..., it will create a new 'DZ' key and its value in new_dict
print ('new_dict=', new_dict)

timesCountry = []
for k,v in new_dict.items():
    timesCountry.append(v)
print ('timesCountry =', timesCountry)


fig, ax = plt.subplots()
ax.set(
    xlabel='country code',
    ylabel='frequency of nobel prize award',
)
ax.bar( country_codes[0:20] , timesCountry[0:20] )
plt.show()



#fig, [ax1, ax2] = plot.subplots(2, figsize=(13, 10))
#temp plot
# fig, ax = plt.subplot()
# heights = []
# for year in x1:
#     heights.append(tempData[year])
# ax.set(
#     xlabel='year',
#     ylabel='global temperature (Celsius) anamoly',
#     )
# x1=list(sorted(tempData.keys() )

# ax.bar( x1 , heights )
# plt.bar( tempData.keys(), tempData.values() )
# plt.show()