from matplotlib import pyplot as plt

#Store some values for X and Y axis
X_values = [23,45,67,80]
Y_values = [120, 30,210,300]

#Use plot method to draw chart using the above values
plt.plot(X_values,Y_values)  # The plot function draws a line chart. we can use "scatter" function instead to get scattered graph
#plt.scatter(X_values,Y_values) #Will plot scatter graph

#If you have large values like world population etc on the x-axis, instead of showing X_values, you can show the values in
# logarithmic form using xscale function Ex: plt.xscale('log'). In this case a value of 10K for example will be shown as 10 power of 4

#Assign labels for X Axis, Y axis and title. You could use variables as well instead of strings as shown below
plt.xlabel("X-Axis name")  #Add X-axis label
plt.ylabel("Y-Axis name")  #Add Y-axis label
plt.title("This is chart title") #Add chart title
plt.grid(True) #Optionally, you can add Grid background to the chart

#Display the chart
plt.show()