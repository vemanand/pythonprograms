''' This is a sample program to use generators in python
Here we define a generator function that returns one value at a time using "yield" '''

#Define a generator function. Notice that this uses "yield" instead of return
def genfun(a):
   for val in a:
       yield val

a = [34,56,78,100]
#Create a generator object by calling the generator function and passing sample List of values
b = genfun(a)
print(type(b)) #You can verify that b is a generator object - class generator

#You can get one value at a time from the generator object by calling "next" method
print(next(b))
print(next(b))
print(next(b))
print(next(b))

#Once all values are retrieved, calling next() will not yield any value, but StopIteratior is called
print(next(b))
