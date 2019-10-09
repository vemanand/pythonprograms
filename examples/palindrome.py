'''
Program to check if a string is palindrome or not
A palindrome is a string which is same when you read forward or backwards.
'''

my_str = input("Enter any string you want to check for palindrome:")

# make it suitable for caseless comparison. you can use lower() as well, but casefold() is recommended as it is more strict
my_str = my_str.casefold()

# reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
   print(my_str," is palindrome")
else:
   print("%s is not palindrome" %my_str)