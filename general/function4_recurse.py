'''
Program to demo recursive function calls (Call the function from within)
'''

#Recursive function that prints all numbers from given number down to 1
def displaynumbers(num):
    if num == 0:
        print("DONE")
    else:
        print(num,end=",")
        displaynumbers(num-1)

displaynumbers(10)

#Recursive function to find the factorial value of the given number
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

print("The factorial of 5 is ",factorial(5))
print("The factorial of 6 is ",factorial(6))