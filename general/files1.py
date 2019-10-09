'''
Sample program to demo file I/O in Python
You can use open() to open a file, read() to read the contents of a file, close() to close the file
This program covers other functions - tell(), seek()
Other read methods are readline(), readlines()
'''

#Open the file. The default mode is "r" - read. Other modes are w - write, a - append, b - binary
testfile = open("../resources/sample.txt")
#Read and print the contents of the file
#This will read the file contents and positions the pointer at the end of file
print(testfile.read())

print("Reading again. The contents are:")
if testfile.read() == "":
    print("No more content. The pointer is at "+str(testfile.tell())+" Move it to the beginning")
else:
    print(testfile.read())

#Use seek(<how many bytes>,<from where>) to move the pointer to the beginning
testfile.seek(0,0) # You can also use seek(0)
print("Reading again after resetting the pointer. The contents are:")
print(testfile.read())

#Close the file
testfile.close()