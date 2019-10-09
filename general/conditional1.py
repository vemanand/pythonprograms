'''
Sample program to demo conditional statements - if, if-else, if-elf-else
Relational operators: >, <, >=, <=, ==, !=
Logical operators: and, or
Arithmetic operators: +, -, *, /, % (modulus or reminder), ** (power or exponentiation), +=, -=, *=, /=, %=
'''
age =  int(input("enter your age: "))

print("You are %d years old" %age)
if (age > 18):
    print("You are eligible to vote")
else:
    print("you are not eligible to vote")

#Write a program to find if the given number is Even or Odd number

print("Now we will compare the values of 2 given numbers")
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

if (n1>n2):
    print("%d is greater than %d" %(n1,n2))
elif (n1<n2):
    print("%d is less than %d" %(n1,n2))
else:
    print("Both the given numbers are equal")

