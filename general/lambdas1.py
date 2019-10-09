'''
A lambda function is an anonymous function in Python. It can take any number of arguments, but can only have one expression.
Use lambda functions when an anonymous function is required for a short period of time.
'''

#A lambda function that adds 10 to the number passed in as an argument, and print the result
val = lambda num: num + 10
print(val(8))

#A lambda function that takes two arguments and returns the product value
mul = lambda n1,n2: n1 * n2
print(mul(5,6))

'''The power of lambda is better shown when you use them as an anonymous function inside another function.
Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number using lambda
You can use that function that always doubles or trples the number you send in as an argument as shown below'''

def myfunc(num):
    return lambda a: num * a

doubler = myfunc(2)
tripler = myfunc(3)

print(doubler(10))
print(tripler(10))