'''
Sample program showing how we can create a series from a list, numpy array and dictionary
The solution is to use Series() method
'''

import numpy as np
import pandas as pd

mylist = list("abcdefghijklmnopqrstuvwxyz")
myarr = np.arange(26)
mydict = dict(zip(mylist,myarr))

ser1 = pd.Series(mylist)
ser2 = pd.Series(myarr)
ser3 = pd.Series(mydict)
print(ser3.head())
