'''
Sample program to display the calendar for the given month & year
This uses "month" function of calendar module
'''

import calendar

year = int(input("Enter the year:"))
month = int(input("Enter the month number:"))

#Display the calender for the given month and year
print("Here is the calender:")
print(calendar.month(year, month))