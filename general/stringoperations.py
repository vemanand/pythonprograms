''''
Sample program showing various String Methods
Strings are immutable - contents cannot be modified

'''
name1="John"  #You can use double or single quotes
name2= str("Abraham")
name3= str() #Empty string
print(name1 * 3)  #Print string 3 times

#Slicing - syntax (startindex:endindex:increment)
str1 = "welcome to Python"
print(str1[2:5]) #Return from 2nd index to 4th index - lco
print(str1[:7]) #Return from start to 6th index - welcome
print(str1[8:]) #Return from 8th index to end - to python


