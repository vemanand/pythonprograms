'''
Drawing Line plot in different colors
Reference:  https://matplotlib.org/3.1.1/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py
'''
import numpy as np
from matplotlib import pyplot as plt

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t*20, 'bs', t, t**3, 'g^')
plt.title("Multiple Line plots")
plt.annotate("Sample annotation",xy=(3,40),xytext=(4, 45),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()