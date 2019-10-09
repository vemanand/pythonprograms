'''
Histogram is used to display frequency across a continuous or discrete variables.
Use cases: #of customers tenure wise - Tenure distribution (How many customers with less than a month, with 10 months, with 20 months tenure etc)
'''
import matplotlib.pyplot as plt

vals = [12,45,33,75,19,55,39,57,6,42,47,52,42,38]

#use hist() function to plot Histogram. Bins represent the markers on X-axis - how we want to plot frequencies
#Y-axis show the number of entries found (frequency) within the given range Ex: There is only 1 value between 0-10, 2 values between 10-20 and so on
#plt.hist(vals,bins=[0,10,20,40,60,80])
plt.hist(vals,bins=[0,10,20,40,60,80],color="#67543f",edgecolor="yellow") #edgecolor, color attributes are common to many plot methods

#Customize
plt.xlabel("Ranges")
plt.ylabel("#of Observations")
plt.title("Histogram Demo")
plt.grid(True)
plt.show()