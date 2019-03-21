import pandas as pd
from functools import reduce
import matplotlib.pyplot as plt
import numpy as np

# Here we will import data according to the set we have choosen
df = pd.read_csv("Consumo_cerveja.csv")


weekendconsumption = df.loc[df['WeekEnd'] == 1]['Consumption']
weekendconsumption_liters = reduce(lambda x,y: x+y, weekendconsumption)
# Here we have the medium beer consumption during the week-ends
mid_consumption_WE = weekendconsumption_liters/len(weekendconsumption)
print( "Medium Consumption WE %s" % mid_consumption_WE)


weekconsumption = df.loc[df['WeekEnd'] == 0]['Consumption']
weekconsumption_liters = reduce(lambda x,y: x+y, weekconsumption)
# Here we have the medium beer consumption during the week
mid_consumption_W = weekconsumption_liters/len(weekconsumption)
print("Medium Consumption Week %s" % mid_consumption_W)


rainconsumption = df.loc[df['Rain'].astype('float') > 0 ]['Consumption']
rainconsumption_liters = reduce(lambda x,y: x+y, rainconsumption)
# Here we have the medium beer consumption during fainy days
mid_consumption_rainy = rainconsumption_liters/len(rainconsumption)
print("Medium consumption on rainy day %s" % mid_consumption_rainy)

norainconsumption = df.loc[df['Rain'].astype('float') == 0 ]['Consumption']
norainconsumption_liters = reduce(lambda x,y: x+y, norainconsumption)
# Here we have the medium beer consumption during sunny days
mid_consumption_not_rainy = norainconsumption_liters/len(norainconsumption)
print("Medium consumption on sunny day %s" % mid_consumption_not_rainy)

boxplot_to_show = {"Week" :weekconsumption.to_list(), "Week-end" : weekendconsumption.to_list(),"rain" : rainconsumption.to_list(), "No rain" : norainconsumption.to_list()}

x = df['TempMed']
y = df['Consumption']


plt.figure(1)
plot1 = plt.subplot(211)
plot1.set_title("Beer consumption in function of temperature")
plt.scatter(x, y)

z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"ro")

x = df['Rain']
y = df['Consumption']
plot2 = plt.subplot(212)
plot2.set_title("Beer consumption in function of rain")
plt.scatter(x, y)

z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"ro")

plt.figure(2)
i = 1
for key,value in boxplot_to_show.items():
    if i >=3:
        plt.figure(3)
        i=1 
    plot = plt.subplot(210+i) 
    i += 1
    plot.set_title("Box plot for %s values" % key)
    plt.boxplot(value, vert=False)
plt.show()