'''
Sample program to find if the given number is an armstrong number or not
A positive integer is called an Armstrong number of order n if abcd... = a power (n) + b poewr(n) + c power(n) + d power(n) + ...
Ex: 153 = 1*1*1 + 5*5*5 + 3*3*3  = 1 + 125 + 27 = 153 is an armstrong number
Exercise: Write a program to print all armstrong numbers below 1000
'''

# take input from the user
num = int(input("Enter a number which you want to verify if it is an Armstrong number or not: "))
# find the number of digits in the given number
order = len(str(num))

# initialize sum
sum = 0
temp = num
while temp > 0:
   digit = temp % 10  #Will give the last digit of the number Ex: 3345 % 10 will give 5
   sum += digit ** order  #Find the digit to the power of order of the number
   temp //= 10 #Will return the number, excluding the last digit Ex: 3345//10 will given 334

# Check if the given number is equal to the sum
if num == sum:
   print(num,"is an ARMSTRONG NUMBER")
else:
   print(num,"is not an Armstrong number")