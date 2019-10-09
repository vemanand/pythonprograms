''' Sample program to define and use generator function'''

#Define a generator function that can yield 2 values
def sample():
    n = 3
    yield n
    n += n
    yield n

#Create generator object by calling the function
val = sample()

#Retrieve values by calling "next" method. StopIteration will be called once all values are retrieved
print(next(val))
print(next(val))
print(next(val))