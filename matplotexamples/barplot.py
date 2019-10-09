'''
Sample program using Bar plot demo
A Bar chart/plot/graph represents categorical data using rectangular bars with height/length proportional to the values.
Use cases: Visualize #of customer per payment method; #of customers per city or type of TV cable network; #of issues based on status;
'''
import matplotlib.pyplot as plt

#Create sample dataset
fruits = {"mango":30,"Cantalop":20,"Strawberry":15,"Banana":35,"Watermelon": 12}

names = list(fruits.keys())
counts = list(fruits.values())

#Use bar() method to plot bar chart. Optionally use color attribute to specify bar color
plt.bar(names,counts,color="maroon")
plt.xlabel("Fruits")
plt.ylabel("Quantity")
plt.title("Fruits Stock")
#Optionally, you can create Horizontal bar plot using barh
#plt.barh(names,counts)

plt.show()