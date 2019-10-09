'''
In python it is possible to use the combination of loop statement and conditional statement
For this, Python has special constructs for-else and while-else.
The else block will be executed once the loop condition is not met or the loop completes its execution.
The else block will NOT be executed when the loop terminates with break
Use this construct when you want to execute some code after the loop statement is done competing all iterations without breaking in between
This sample program demos both these constructs
'''

for i in range(3):
    print("For loop")
else:
    print("For loop else block - without break")

for i in range(3):
    print("for loop with break")
    if (i==1):
        break
else:
    print("For loop else block - with break")

i = 1
while (i<5):
    print("While loop")
    i +=1
else:
    print("While loop else block - No break")

i=1
while True:
    print("While loop with break")
    i+=1
    if (i==2):
        break
else:
    print("While loop else block - with break")