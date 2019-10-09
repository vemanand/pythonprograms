'''
Program to count the number of each vowel in a given string
'''

# string of vowels
vowels = 'aeiou'

# Initialize a string or take string from user using input() method
givenstr = 'Hello, have you tried our turorial section yet?'

# make it suitable for caseless comparision using casefold() method
# casefold() is similar to lowe() method that it converts all characters to lower case
# but casefold() is much strict and can convert other language characters as well for case less comparison
givenstr = givenstr.casefold()

# make a dictionary with each vowel a key and value 0
vowel_dict = {}.fromkeys(vowels, 0)
print(vowel_dict)

# parse through the given string. Check if each character is vowel. If yes, increment the value for that vowel key in the above dictionary
for char in givenstr:
   if char in vowel_dict:
       vowel_dict[char] += 1

print(vowel_dict)