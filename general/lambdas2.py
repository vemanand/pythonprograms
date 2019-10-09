'''
Sample program to demo lambda, map, filter, reduce functions
Lambda functions doesn't use def and return statements, but the lambda keyword
MAP function will apply the defined (lambda or custom) function to each of the elements of a sequence and returns the updated/modified sequence
FILTER function will filters items out of a given sequence based on the given condition and returns the filtered list
REDUCE function applies the same operation to each item of a given sequence, uses the result of the operation as a first parameter to next operation and so on
the reduce function returns an item after applying all operations, NOT a list
'''
def normalmax(x,y):
    if x > y:
        return x
    else:
        return y

#Lambda function to find the Maximum of given 2 numbers
lambda_max = lambda x,y: x if x>y else y

print("Lambda function demo")
print(normalmax(34,56))
print(lambda_max(22,15))

#Regular function to square the numbers of the given list
def normalsquare(list1):
    list2 = []
    for num in list1:
        list2.append(num ** 2)
    return list2

list1 = [3,5,6,2,7]
print("Map function demo")
#Call the regular method to get squares
print(normalsquare(list1))
#Use the MAP with lamba function to get the squares
print(list(map(lambda num: num ** 2, list1)))
#Use the MAP with regular function to get the squares
#print(list(map(normalsquare,list1)))
#Accomlish the samething using List comprehensions
print([x **2 for x in list1])

def normal_even(mylist):
    evenlist = [num for num in mylist if num%2 == 0]
    return evenlist
#Declar a list from which we want to get the even numbers
mylist = [34,56,67,31,22,20,55,47]
print("Filter function demo")
#Call regular function to get the even numbers
print(normal_even(mylist))
#Call map function to get the even numbers
print(list(filter(lambda x: x %2 ==0, mylist)))
#Use list comprehension to get the same thing done
print([x for x in mylist if x %2 == 0])

#Regular function to returns the product of all numbers of the given list
def prodlist(plist):
    prod = plist[0]
    for i in range(1,len(plist)):
        prod *= plist[i]
    return prod

#From python 3.x.x reduce is moved to functools
from functools import reduce
print("Reduce function demo")
plist = [2,3,4,5]
print(prodlist(plist))
print(reduce(lambda a,b: a*b, plist)) #Here lambda function is applied to each pair of items in the list. 2 X 3 = 6, 6 X 4 = 24, 24 X 5 = 120