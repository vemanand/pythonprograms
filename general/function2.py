'''
A function can accept multiple values as parameters by making use of pointers
A single pointer is used for this purpose: *args
'''

#Method that can accept any number of arguments.
#The argument values are treated as a List of values
def anyargs(*params):
    for i in params:
        print(i, end=",")
    print("number of arguments = "+str(len(params)))

#Multiple ways you can call the above function
anyargs("One")
anyargs(3,4,5)
anyargs("this","is","test",45)  #Arguments of different types
anyargs([45,67,10,22]) #One argument with List
anyargs() #Zero arguments

#Method that takes 2 mandatory parameters and optional arguments there after
#Notice the use of Placeholders for printing
#The "%" operator is used to format a set of variables enclosed in a "tuple" together with a format string
def multiargs(first, second, *therest):
    print("First: %s, Second: %s" %(first,second))
    print("And the other arguments are... %s" % list(therest))

#Different ways you can call the above function
multiargs(3,4,5,6,"name","hi",56.7)
multiargs(10,20)

# This method simply returns the number of arguments after 3rd one.
# The 3rd argument is optional and has a default value
def foo(a, b, c="third", *args):
    print("3rd arg value = "+str(c))
    return len(args)


# test code for the above method
if foo(1,2,3,4) == 1:
    print("Good.")
if foo(11,12,13,14,15) == 2:
    print("Better.")
if foo(21,22) == 0:
    print("No additional arguments")

def multiply(*args):
    '''*args is a function prototype that can accept varying number of arguments
    General multiplication function that can multiply any set of given numbers'''
    m = 1
    for num in args:
        m = m * num
    return m

print(multiply(2,3))
print(multiply(4,3,2))
print(multiply(10,20,30,3))
digits = len(str(multiply(345,6785,3444,22334324,2343434,23333,3243423,23323,34212,567)))
print("Number of digits = ",str(digits))