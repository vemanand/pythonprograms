''''
Sample program to convert decimal to Binary format
We will write two solutions - one using recursive function and another using built-in function
'''

decimal = int(input("What number you want to convert to Binary? "))

def convertobinary(num):
    if num > 1:
        convertobinary(num//2)
    print(num%2, end='')

convertobinary(decimal)

print("\nUsing built-in function bin(), the binary equivalent of %d is %s" %(decimal,bin(decimal)))