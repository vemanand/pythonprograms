'''
Sample program to demonstrate different SET operations
Python offers a datatype called set whose elements must be unique. Set must be declared using curly/flower brackets
It can be used to perform different set operations like union, intersection, difference and symmetric difference.
'''

# define two sample sets
SET1 = {0, 2, 4, 6, 8, 10}
SET2 = {1, 2, 3, 4, 5, 6}

# set union
print("Union of two sets is", SET1 | SET2)

# set intersection
print("Intersection of sets is", SET1 & SET2)

# set difference. First set minus second set = Unique elements of set1
print("Difference of sets is", SET1 - SET2)

# set symmetric difference. Unmatched/Uncommon entries from both the sets
print("Symmetric difference of sets is", SET1 ^ SET2)