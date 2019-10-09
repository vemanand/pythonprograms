'''
Sample program showing best practices in coding

'''

#Practice1 - Retrieving sequence values along with index
#When you want to get the elements of a sequence along with index/position, use enumerate() method as shown below
cities = ["Mumbai", "Hyderabad", "Chennai", "Bengaluru"]
for i, city in enumerate(cities):
    print (i, city)

#Practice2 - Traversing through 2 or more Lists together
#When you want to traverse through 2 or more sequences simultaneously, use zip() method
students = ["rakesh", "murali", "jahnavi", "bharath"]
marks = [48,40, 35, 49]
for s,m in zip(students,marks):
    print(s,m)

#Practice3 - While swaping 2 variables values
#If you want to swap two variable values, use below code instead of using a 3rd temporary variable
a,b =45, 33
print("Before: a=%d and b=%d" %(a,b))
a,b = b,a
print("After: a=%d and b=%d "%(a, b))

#Practice4 - Working with dictionary retrieval
#when you want to retrieve a key value from a dictionary, but not sure if the key exists and would like to assign some default value
#in that case use "get" method instead of writing code to check for key (if 'key' in dict:)
employees = { "John":45, "Mike": 40, "Lynda":36}
age = employees.get("Mike", "unknown") #this will assign unknown value in case the key doesn't exist in the dictionary
print("Mike's age = %s years" %age)
print("Mary's age = %s years" %employees.get("Mary", "Unknown"))

#Practice5 - While checking if a value exists in a given list or not
#When you want to check for a value in the list, use "else" statement with/of for loop
checkfor='y'  #Chane this value to check both positive and negative scenarios
letters = ['a','e','i','o','u']

print("Finding out if the given letter is found in the list or not - Normal way")
#the normal way
found = False
for let in letters:
    if (checkfor == let):
        found = True
        print("Found")
        break;

if not found:
    print("Not found")

#the correct and easy way - use else statement with for loop
print("Finding out if the given letter is found in the list or not - Correct way")
for let in letters:
    if (checkfor == let):
        print("Found")
        break
else:  #Will be executed only if no break occurs in the loop OR only after the entire loop is executed properly
    print("Not found")

#Another better way
print("Better and simple way to find value in the list")
print(['Not Found', 'Found'] [checkfor in letters])

print("Many options to find value in the list")
print('Found' if checkfor in letters else "Not Found")

#Practice6 - Reading file to process each line
#When you want to read a file and process each line, instead of coding the logic yourself just use for loop on the file object
#after the file is open, as file object is an iterator object
'''
#Regular/Normal way
myfile = open("../resources/lyrics.txt")
print("Reading and processing file content line by line:")
print("Normal Way")
text = myfile.read()
for line in text.split('\n'):
    print(line)
myfile.close()    
'''

'''
#Better way. Remember file object is iterable and use for loop to iterate. Close later
print("Better way of reading file line by line - use file object as iterator")
for line in myfile:
    print(line)
myfile.close()
'''

'''
#Best way - Use "with" statement. You don't need to clean-up/close. It will be handled automatically
print("Best way of reading file line by line - using WITH along with for loop")
with open("../resources/lyrics.txt") as myfile:
    for line in myfile:
        print(line)
'''

#Another option to read file and process each line - the simplest way
for line in open("../resources/lyrics.txt"):
    print(line)

#Practice7 - Proper exception handling
#Handle exceptions properly using try-except-else-finally construct as shown in exception1.py file