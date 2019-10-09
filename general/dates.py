'''
datetime module of python can be used to work with date types.

'''
import datetime

#Print the current date & time using now() method
dateval = datetime.datetime.now()
print(dateval)

#We can use the class constructor to create a date. The constructor takes 3 parameters - year, month and day all in numbers
d1 = datetime.datetime(1974,4,9)
print(d1)

'''
We can use strftime() method to format the date object. It takes one parameter - format, to format the date string
Some of the format parameters you can use are:
%a, %A - Week day short version and long version
%b, %B - Month name short version and long version
%y, %Y - Year short version and full version
%H - Hour in 24 hr format (00-23)
%I, %p - Hour in 12 hr format,  AM/PM
%S - second (00-59)
%Z - timezone
%j - day number of the year (001-366)
%c - Local version of date and time
%x %X - Local verion of date, Local version of time
%w - Weekday as number from 0-6, sunday being 0
%d, %m - day of month in number (01-31), month as a number (01-12)
'''
print(dateval.year)
print(dateval.strftime("%B %d %A"))