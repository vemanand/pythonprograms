'''
Sample program to draw Doughnut plot. For this, we create 2 pie charts and combine those. The inner pie is filled with white color to get required effect.
A doughnut chart is used to show the Area/Measurement of each category
Using the same dataset as piechart.py
'''

from matplotlib import pyplot as plt

#Sample data
animals = ["frogs",'dogs','cats','rats','chickens']
sizes = [10,30,20,7,25]
inner_pie = [5]
drcolors = ["#4567ab",'#23334f','#1267bc',"yellow","black"]

#Optionally you can fix the plot size
plt.figure(figsize = (10,7))

#customized pie plot. Explode should have the same number of values as the categories
plt.pie(sizes,labels=animals,radius=1.0,colors=drcolors)
#Draw inner piechart
plt.pie(inner_pie,radius=0.5,colors='w')
plt.title("Custom Doughnut Chart")
#Save transparent figure. The keyword argument transparent which, if 'True', will make the figure and axes backgrounds transparent when saving.
plt.savefig("../output/doughnut_transparent.png",transparent=True)
plt.show()