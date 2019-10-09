'''
Sample program showing Stream Plot for wind analysis. It is a 2D plot used to show fluid flow and 2D field gradients.
Applied in Physics - windtrend analysis
'''
import numpy as np
import matplotlib.pyplot as plt

#Prepare sample data
'''
x = np.arange(0,10)
y = np.arange(0,20,2)
x1, y1 = np.meshgrid(x,y)
u = np.ones((10,10))
v = np.zeros((10,10))
'''

x = np.arange(0,2.2,0.1)
y = np.arange(0,2.2,0.1)
x1, y1 = np.meshgrid(x,y)
u = np.cos(x1)*y
v = np.sin(y1)*x

#Add axes
ax1 = plt.subplot()
ax1.streamplot(x1,y1,u,v,density=0.8)
plt.title("Stream plot demo")
plt.show()