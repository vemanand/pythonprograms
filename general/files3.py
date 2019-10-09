'''
This program demonstrates other file operations. files1.py covered Read and files2.py covered append, write operations
This program will make use of both to create one file from another
The OS module has additional file operations.
os.reaname(<current nanme>,<new name>) - to rename a file
os.remove(<filename>) - to delete a file
'''
import os
os.rename("../resources/sample.txt", "../resources/rensample.txt")

readf = open("../resources/rensample.txt")
copyf = open("../resources/copysample.txt","w+")
contents = readf.read()
print("contents of renamed sample file are:\n"+contents)
copyf.write(contents)
copyf.seek(0)
print("contents of copied file are:\n"+copyf.read())
readf.close()
copyf.close()

#Rename the file back to its original name and delete the copied file
os.rename("../resources/rensample.txt","../resources/sample.txt")
os.remove("../resources/copysample.txt")
print("Renamed to original name and deleted copied file successfully")


