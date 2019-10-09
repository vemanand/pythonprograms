'''Sample program to demo generator function
This program uses for loop to retrieve all values at once instead of calling next() method'''

import random

#Define a generator function that will return 7 values
def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1,15)

#Instead of creating generator object and calling "next" again and again, you cal call all values at once using for loop
#Note that this will display only 7 values, since the generator function yields only 7 numbers
for random_number in lottery():
    print("The next number is... %d!" %(random_number))