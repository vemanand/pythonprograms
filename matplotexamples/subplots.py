'''
Many plots can be combined together in one figure. This sample program shows multiple subplots
Reference: https://matplotlib.org/3.1.1/tutorials/introductory/sample_plots.html#sphx-glr-tutorials-introductory-sample-plots-py
'''
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
data = np.random.randn(2, 100)

fig, axs = plt.subplots(2, 2, figsize=(5, 5))
axs[0, 0].hist(data[0])
axs[1, 0].scatter(data[0], data[1])
axs[0, 1].plot(data[0], data[1])
axs[1, 1].hist2d(data[0], data[1])

plt.show()