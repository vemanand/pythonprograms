import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,10,1)
y1 = 2*x+5
y2 = 3*x+7

#Use subplot to create two or more plots
plt.subplot(1,2,1)  #rows,cols,position
plt.plot(x,y1)
plt.title("First graph")

plt.subplot(1,2,2)
plt.plot(x,y2)
plt.title("Second graph")

plt.show()