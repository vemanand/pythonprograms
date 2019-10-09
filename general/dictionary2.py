'''
Dictionaries can be iterated over, just like a list.
However, a dictionary, unlike a list, does not keep the order of the values stored in it.
Some Dictionary functions are
'''
phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

#Display the number of elements in the dictionary using len()
print("Number of items in phonebook = %d" %len(phonebook))

#To remove any pair you can use del or pop methods
del phonebook["Jack"]
phonebook.pop("John")
print(phonebook)

#You can add new values to dictionary
phonebook["Jimmy"] = 8942323342
print(phonebook)

#Test for entries
if "Jack" not in phonebook:
    print("Jack is not present in phonebook")
if "Jimmy" in phonebook:
    print("Jimmy is present in phonebook")