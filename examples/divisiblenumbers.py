'''
Sample program to show all the numbers divible by a given number out of a List of numbers
Here we use anonymous function which is defined by using "lambda" keyword
A lambda function can take any number of arguments, but can only have one expression.
'''

# Assume a list of numbers
my_list = [12, 65, 54, 39, 102, 339, 221,660]
print("Given list of numbers: "+str(my_list))
# use anonymous function to filter all the numbers that are divisible by 13 from the list
result = list(filter(lambda x: (x % 13 == 0), my_list))

# display the result
print("Numbers divisible by 13 are",result)