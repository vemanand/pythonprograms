'''
Sample program showing Violin polot demo.
Used to show probability density function - Within the given range, what is the probability for a specific value to be present
Violin plot allows to visualize the distribution of a numeric variable in several groups. Used when the amount of data is huge
and showing individual observations becomes difficult
'''
import matplotlib.pyplot as plt

total =[12,9,22,31,27,44,67,75,34,50]
order = [2,5,14,12,18,8,11,15,25,30,22,44,28]
discount =[2,1,4,6,5,8,9,2,6,4,14,25,34]
data =list([total,order,discount])
plt.violinplot(data,showmeans=True, showmedians=True)

#Customize plot
plt.title("Violin plot demo")
plt.xlabel("Datasets")
plt.ylabel("Range of values")
plt.grid(True)
plt.show()