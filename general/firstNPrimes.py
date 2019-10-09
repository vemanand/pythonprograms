'''
Sample program to display the first N prime numbers - uses custom function, for loop, while loop
Note: Any number that is divisible ONLY by 1 & the number itself is a Prime number
'''

#Helper function that will return if the given number is a prime number or not
def isprime(num):
    for i in range(2,num):
        if (num %i == 0):
            return False
    return True

#Take input from the user to know how many prime numbers are required
count = int(input("\nHow many prime numbers you want to print starting from 1? "))

#Empty list to store the list of primenumbers found
primenumbers = []
primenumcount = 0
num = 1

#Loop until we find the required number of prime numbers
while (primenumcount < count):
    if isprime(num):
        #Check if the prime number already exists in the list. Add it otherwise and increment primenumcount
        if not primenumbers.__contains__(num):
            primenumbers.append(num)
            primenumcount += 1
    num = num + 1
print("The first %d prime numbers are " %count,end=":")
print(str(primenumbers))