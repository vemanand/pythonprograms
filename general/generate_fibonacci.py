''' Program to illustrate Generators in Python
We will generate a Fibonacci series - starts with 0, 1 and each fibonacci number is the sum of two preceding numbers
We will also try to generate a series of Even numbers and display the same
'''

#define a generator function that yields unlimited Fibonacci series
def fibonacci():
    first,second = 0,1
    while True:
        yield  first
        first,second = second, first+second

#Call the generator function using for loop and display values
for i in fibonacci():
    print(i,end=" ")  #Display the values separated by a space
    # Break out of the loop once the series exceeds some value, 50 for example
    if i > 50:
        break

#Declare a variable to store a range of even numbers - starts at 2, ends at 100 excluding 100, increatement by 2
vals = range(2,100,2)
#Defind generator expression to store all values
numbers = (n for n in vals)
print(numbers)
for i in numbers:
    print(i,end=",")  #Print comma separated values
