'''
Custom functions can be written using "def" keyword in python
This program has several functions. A function may have Zero or more arguments.
"return" keyword is used to return a value from the function. "pass" statement doesn't do anything
'''

#custom function sample without any arguments - just prints the message Hiiii
def sayHi():
    print("Hiiiii!")

##custom function sample with one argument - just prints the message that is passed as parameter
def showMessage(msg):
    print(msg)

#Two argument function that simply prints a message
def greet(name, greeting):
    print("Hello ",name,"... ",greeting)

#This function returns the sum of given numbers
def add(n1,n2):
    return n1+n2

#This is a do nothing function because "pass" is a dummy statement
def dummy():
    pass

sayHi()
showMessage("This is a custom function")
greet("Anand", "Good morning")
print(add(30,55))
print(add(34.56,22.55))
dummy()