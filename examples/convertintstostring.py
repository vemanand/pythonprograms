'''
A list of integers can be converted to a String using "join" function
Sample program showing the same - converting a given list of numbers to comma separated String values
'''

a=[1,2,3,4,5,6]
numbers = ",".join(str(i) for i in a)  #remove comma if you don't want to separate values by comma
print(numbers)
print(len(numbers))