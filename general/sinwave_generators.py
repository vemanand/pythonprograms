''' This program demonstrates the display of sine waves using a normal function and a generator function
You can notice that while the regular function returns all results at once, the generator returns one result at a time
'''

import numpy as np
from matplotlib import pyplot as plt

#This function will draw all 4 sin waves at once
def sinefuc(flip = 2):
    x = np.linspace(0,14,100)
    plt.title("All sine waves")
    for i in range(1,5):
        plt.plot(x,np.sin(x + i*0.5) * flip)

#Call the function to get all sine waves at once
sinefuc()
plt.show()

#This function will yield one sin waves at a time
def generatorsine(flip = 2):
    x = np.linspace(0,14,100)
    plt.title("One sine wave at a time - generator")
    for i in range(1,5):
        yield(plt.plot(x,np.sin(x + i*0.5) * flip))

#Call the generator function that will yield one sine wave at a time
wave = generatorsine()
#The sine ways will be plotted based on the number of times you call the "next" method until all results are retrieved
next(wave)
next(wave)
plt.show()
