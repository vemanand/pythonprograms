'''
Sample program showing how we can compute the Euclidean distance between two series
2 solutions are shown
'''
import numpy as np
import pandas as pd
ser1 = pd.Series([1,2,3,4,5,6,7,8,9,10])
ser2 = pd.Series([10,9,8,7,6,5,4,3,2,1])

#Solution1 - regular formula
print(sum((ser1-ser2) **2)**.5)
#Solution2 - using Numpy function
print(np.linalg.norm(ser1-ser2))