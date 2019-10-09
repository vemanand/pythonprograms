'''
Sample program to demonstrate the command line arguments. It is possible to pass values to a python program from the command line.
You can run the program from command line Or gives values within Pycharm:
select the file (python program) to which you want to pass values -> Run menu -> Edit Configurations ->
Provide the values in "Parameters" field seperated by a space.
Then these command line values can be accessed from the program using sys.argv which returns a List of values, starting with the program name
'''
import sys

print("The values passed from the command line are: ")
def printcommandlineargs():
    for i in range(1,len(sys.argv)):
        print(sys.argv[i], end=",")

#__name__ is a predefined/special python variable that calls the __main__ method whenever a program is ran.
# You can use this to call your own methods/functions as shown below
# You can also use this to call/import specific methods from a module
print("\nThe value of __name__ is \""+__name__+"\"")
if __name__ == '__main__':
    printcommandlineargs()

