'''

'''
import numpy as np
import matplotlib.pyplot as plt

def func(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure()
plt.subplot(211)
plt.plot(t1, func(t1), 'bo', t2, func(t2), 'k')
plt.title("Plot1")

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.title("Plot2")
plt.show()