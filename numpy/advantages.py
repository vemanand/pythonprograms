'''
This sample program shows the advantages of using Numpy arrays
Numpy arrays occupies less memory, faster and more convenient than Lists
'''
import numpy as np
import sys
import time

#Define a list and display its size - memory occupied by the list
myl = range(1000)
print(myl)
print("Size of list = ",sys.getsizeof(2)*len(myl)) #Multiple the length of List with the size of an integer

#Define a numpy array
a = np.arange(1000)
print("Size of numpy array =",a.size * a.itemsize)

#Sample functtion to parse 2 Lists and store the sum of the values in 3rd List
#List stores references that takes memory and then we need to go to the reference location to fetch values, which takes time
def usingList():
    t1 = time.time()
    x = range(100000)
    y = range(100000)
    z = [x[i]+y[i] for i in range(len(x))]
    return time.time() - t1

#Sample function to parse 2 Numpy arrays (NDArray) and store the sum in 3rd array
#NDArray stores the values directly and consumes less memory. Since we can retrieve values directly, it is Faster
def usingNumpy():
    t1 = time.time()
    a = np.arange(100000)
    b = np.arange(100000)
    c = a+b #More convenient than a list
    return time.time() - t1

list_time = usingList()
numpy_time = usingNumpy()
print(list_time," ",numpy_time)
print("In this example Numpy array is ",str(list_time/numpy_time)," times faster than a List")