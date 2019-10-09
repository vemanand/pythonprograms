'''
Demo program showing how we can return positions of the numbers that are multiples of 3 from a series
'''
import pandas as pd
import numpy as np

ser1 = pd.Series(np.random.randint(1,20,8)) #Returns 8 random numbers between 1 and 20
print("Series: %s" %ser1)
print("Index of the numbers that are multiple of 3: %s" %np.argwhere(ser1 %3 ==0))