'''
Sample program to draw area plot. Stackplot is used to plot an area plot
'''

import matplotlib.pyplot as plt

#Define sample dataset
xvals = range(1,16)
yvals = [4,6,8,3,9,14,10,12,7,20,25,15,30,14,22]

plt.stackplot(xvals,yvals,color="green",alpha=0.8)
#Optionally merge with Line plot to show coordinates and borders clearly
plt.plot(xvals,yvals,color="blue")
plt.title("Area plot using Stackplot")
plt.grid(True)
plt.show()
