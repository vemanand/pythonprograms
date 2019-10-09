'''
Arguments in python are passed by reference.
This means any change done in the function on the object are reflected on the original object.
Sample program showing the same
'''

#Function that takes list and modifies it. Original object modified
def myfunc1(list):
    list[0]= 34

list1 = [1,2,3,4]
myfunc1(list1)
print(list1)

#Function that takes list and copies it. Orignal object unchanged
def myfunc2(list):
    list = [3,4,50,60] #A new object is created
list2 = [3,4,5,6]
myfunc2(list2)
print(list2)