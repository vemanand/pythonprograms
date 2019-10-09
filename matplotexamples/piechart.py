'''
Pie chart is used to show percentage or proportional data. Good when we have less than 10 categories
This sample program draws pie chart twice using same dataset - Normal and Customized
'''

from matplotlib import pyplot as plt

#Sample data
animals = ["frogs",'dogs','cats','rats','chickens']
sizes = [10,30,20,7,25]

#Optionally you can fix the plot size
plt.figure(figsize = (10,7))

#Add axes
ax1 = plt.subplot(1,2,1)
#Normal pie plot
ax1.pie(sizes, labels = animals)
plt.title("Simple Pie Chart")
ax1 = plt.subplot(1,2,2)
#customized pie plot. Explode should have the same number of values as the categories
ax1.pie(sizes, labels = animals, shadow = True,autopct = "%1.1f%%",startangle = 90,explode = (0.1,0.15,0,0,0.08),colors=["blue","yellow","red","maroon","pink"])
plt.title("Custom Pie Chart")
plt.show()