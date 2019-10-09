'''
Sample program showing how to draw a color chart - background color, Chart color, Line color and Title colors
2 options are available for background/canvas color and chart/graph color. Comment/Uncomment the code accordingly
'''
import matplotlib.pyplot as plt

#Declare and set Figure color - Option1
#figure = plt.figure(facecolor="yellow")

#Declare and set Figure/Canvas color - Option2
figure = plt.figure()
figure.patch.set_facecolor('green')

#Set Chart/Graph color - Option1
#plt.rcParams['axes.facecolor'] = 'blue'

#Set chart/graph color - Option2
ax = plt.gca()
ax.set_facecolor('#3d2f3c')

#Draw color line
plt.plot([1,2,3],c="maroon")

#Colored Title with given fontsize, alignment
plt.title("Sample line chart",c="w",fontdict={'fontsize':30},loc='right')

plt.show()