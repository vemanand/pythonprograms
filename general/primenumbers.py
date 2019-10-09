'''
sample program demonstrating "for" loop to display all prime numbers below the given number
'''
val = int(input("Enter a number upto which you want to display all Prime numbers: "))
print("All the prime numbers below %d are: "%val)
for num in range(1,val):
    prime = True
    for i in range(2,num):
        if (num % i == 0):
            prime = False
            break
    if prime == True:
        print(num, end=", ")