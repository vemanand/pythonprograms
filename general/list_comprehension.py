'''Sample program showing List Comprehension. It creates a new list based on another list, in a single, readable line.
Makes use of generator expression sytax but using List (Square brackets instead of regular brackets)
1) We will generate the length of list of words from another list, except for the word "the"
2) We will generate a list of integer numbers from another list, but only positive numbers
'''

#Create some string with any sentence
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split() #Will store the list of all words in this variable

#Use list comprehension to create one list from other in a single line
#Here we try to generate the destination list with the length of each word from source list, except for "the"
word_lengths = [len(word) for word in words if word != "the"]
print(words)
print(word_lengths)

#Create a list of numbers including float and negative numbers
numbers = [34,56,37.896,23.14,-45,-2,55.17,12.5]
#Use list comprehension to create another list - store int numbers which are positive
int_numbers = [int(num) for num in numbers if num > 0]
print(numbers)
print(int_numbers)