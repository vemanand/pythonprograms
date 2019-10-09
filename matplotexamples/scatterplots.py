'''
Scatter plots are used to plot data points to show how much one variable is affected by another.
This helps in visualizing the correlation among values/variables.
If the values are together then they have high correlation and if they are widespread they have low correlation and independent.
'''
import matplotlib.pyplot as plt

#Creating sample dataset
a=[10,20,30,40,50,60]
b=[5,11,7,9,34,22]
c=[9,15,26,30, 43,51]

#Create simple/default scatter plots
#plt.scatter(a,b)
#plt.scatter(a,c)
plt.title("Scatter Plots")

#Create custom scatter plots
plt.scatter(a,b,c="black",s=200, edgecolors="r",marker='+',alpha=1.0) #marker values can be 1,2,3,4,0,+
plt.scatter(a,c,color="y",s=300,edgecolors="b",marker="4",alpha=0.8)
plt.grid(True)
plt.legend(['b','c'],loc='best')
#Save the plot for sharing or printing
plt.savefig("../output/scatterplot.png")

plt.show()
