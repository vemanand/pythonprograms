'''
Sample program to sort words of a given string in Alphabetical order (lexicographically)
'''

# Initialize a string or take it as inplut() from the user
my_str = "this is an example program to sort the words in a string"

# breakdown the string into a list of words using split()
words = my_str.split()

# Sort of values of the List
words.sort()

# display the sorted words
print("The sorted words are:")
for word in words:
   print(word)