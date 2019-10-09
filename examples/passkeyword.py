'''
"pass" keyword is used to write the filler code. Use it when there is a syntactic requirement, but no operational/functional requirement
This sample program demos the use of pass keyword
'''

mystr = "a m a z o n"
print(mystr)
#the below loop will display the given string ignoring/removing the spaces
for i in mystr:
    if i == " ":
        pass #Don't do anything when you there is space
    else:
        print(i,end="")

#Do nothing function
def myfun():
    pass
myfun()

