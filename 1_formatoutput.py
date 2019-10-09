'''
variables can be declared to store values. The variable simply refers to a temporary memory location. Type will be determined at run time
The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), together with a format string
%s - String or any object with String representation, %d - integers, %f - float, %.<digits>f - Float numbers with fixed amount of digits after decimal
%x or %X - Integer numbers in Hex representation - Lower case or Upper case
This program shows multiple examples of declaring variables and displaying values using string formatting
'''

# This prints out "Hello, John!"
name = "John"
print("Hello, %s!" % name)

# This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))

# This prints out: A list: [1, 2, 3]
mylist = [1,2,3]
print("A list: %s " %mylist)

#Declare variables with values
data = ("John", "Doe", 53.445)
greet = "Hello"

#Format to get output as "Hello John Doe. Your current balance is $53.44.
print("%s %s %s. Your current balance is $%s." %(greet,data[0], data[1],data[2]))
#Optionally you can convert the value to Float and display
print("%s %s %s. Your current balance is $%.2f." %(greet,data[0], data[1],data[2]))
#The simplest way is to declare a format string and print it
format_string = "Hello %s %s. Your current balance is $%s."
print(format_string %data) #Python will automatically retrieve values from data tuple in sequence

#\r denotes raw String in Python. This means the string followed by \r is considered as it is ignoring the escape sequences
newline = r'\n'
print("The new line character in python is",newline)