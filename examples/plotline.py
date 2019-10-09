'''
Demo program showing a simple line plot
'''
import matplotlib.pyplot as plt

plt.plot([1,2,3,4])
plt.plot([10,20,30,40],lw=3) #Set Line width using lw argument
plt.show()