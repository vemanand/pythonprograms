
#Dine a variable that contains some range of values
rangevals = range(5)

#Define a generator expression that returns a list of values (use square brackets) and stores in the variable
#This is also referred as "List Comprehension" where we create one list from another
# Note that we are incrementing each value by 2, before storing
v1 = [x+2 for x in rangevals]
#print the list - Since this is list comprehension, the type will be list
print(type(v1))
print(v1)

#Define a generator expression that returns a generator object (use regular brackets) and stores the stream in the variable
v2 = (x+2 for x in rangevals)
print(type(v2)) #you can see that the variable is of generator class
print(v2) #you can see that this is a generator object created using generator expresssion

#Write a for loop to get all values from the generator object and display
for i in v2:
    print(i,end=":") #Print each value separated by a colon
