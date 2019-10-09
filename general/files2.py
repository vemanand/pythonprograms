'''
Sample program to show file operations - append & write
We will use the file used in files1.py to append contents to it
Create a new file for writing. Methods used are - open(), read(), write(), seek(), close()
'''
#Open the file in append mode and for reading using "a+" mode because "a" will only allow append, but not read
myfile = open("../resources/sample.txt","a+")
#Write contents using write() method which will append to the file
myfile.write("\nappending a new line - fist time")
#Move the pointer to the beginning. Read and display the contents
myfile.seek(0)
print("The new file contents after appending are:")
print(myfile.read())
myfile.close()

#Open the file file write and read - w+. This will overwrite the file contents if the file exits, otherwise creates a new file.
myfile = open("../resources/sample.txt","w+")
myfile.write("Python is a great language. \n It has features of an object oriented language with huge set of packages\n I love python.")
print("The file contents after writing are:")
myfile.seek(0)
print(myfile.read())
myfile.close()