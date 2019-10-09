'''
Sample program to demo exception handling - the keywords "try, except, else, finally" are used to handle exeptions
Several constructs are possible: try, try-except, try-except-else, try-except-else-finally, try-except-finally, try-finally
comment and uncomment the int() conversion statements below to check the behavior in both Normal and Exception cases
'''

print("Convert to Int - No excepion handling - WORST")
print(int('1')) #this will work as character 1 will be converted to integer 1
#print(int('A')) #this will give error (ValueError) as character A cannot be converted to integer. The program will terminate here, if we don't handle the exception
print("Done") #this statement won't be executed when there is an exception above

print("Convert to Int - Handling exception - NORMAL")
try:
    #print(int('1')) #this will work as character 1 will be converted to integer 1
    print(int('A')) #this will give error (ValueError) as character A cannot be converted to integer. The program will terminate here, if we don't handle the exception
except: #the program will not terminate in case of exception. The below statements will be executed in that case
    print("Conversion failed")
print("Done")

print("Convert to Int - Handling exception with else - GOOD")
try:
    print(int('1')) #this will work as character 1 will be converted to integer 1
    #print(int('A')) #this will give error (ValueError) as character A cannot be converted to integer. The program will terminate here, if we don't handle the exception
except: #the program will not terminate in case of exception. The below statements will be executed in that case
    print("Conversion failed")
else: # Will be executed in NO Exception case
    print("Conversion successful")
print("Done")

print("Convert to Int - Handling exception with else and finally - BETTER")
try:
    #print(int('1')) #this will work as character 1 will be converted to integer 1
    print(int('A')) #this will give error (ValueError) as character A cannot be converted to integer. The program will terminate here, if we don't handle the exception
except: #To handle exceptions. The program will not terminate in case of exception now. The below statements will be executed in that case
    print("Conversion failed")
else: # Will be executed in NO Exception case only
    print("Conversion successful")
finally: #Will always be executed whether there is an exception or not. Clean up code goes here
    print("Done")
