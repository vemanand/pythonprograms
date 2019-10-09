'''
Sample program showing how we can get elements NOT common to the given 2 series
Demos the use of Union and Intersect
'''

import pandas as pd
import  numpy as np

ser1 = pd.Series([1,2,3,4,5])
ser2 = pd.Series([4,5,6,7,8])
print("Series1 = %s"%ser1)
print("Series2 = %s"%ser2)
union_ser = pd.Series(np.union1d(ser1, ser2)) # Returns Unique series - 1,2,3,4,5,6,7,8
#print("Union of the series = %s" % union_ser)
intersect_ser = pd.Series(np.intersect1d(ser1,ser2)) #Returns intersection of the series - 4,5
#print("Series intersection - items common to both series = %s" %intersect_ser)
print("Items not common to series: %s" %union_ser[~union_ser.isin(intersect_ser)])