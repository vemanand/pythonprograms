'''
Sample program showing Boxplot demo.
Used to see IQR (Inter Quartile Range). Quartiles - Q0, Q1, Q2, Q3. The max value Q4 may be left out
Boxes will be bigger if the data range is more for a given dataset (max value - mix value)
Box plot is helpful in viewing the dataset summary and in doing outlier analysis
'''
import matplotlib.pyplot as plt

total =[12,9,22,31,27,44,67,75,34,50]
order = [2,5,3,14,12,18,4,8,11,15,48] #This dataset has outlier 48
discount =[2,1,4,6,5,8,9,2,6,4,32] #This has outlier 32
data =list([total,order,discount])
plt.boxplot(data,showmeans=True)

#Another boxplot with datasets declared inline
#plt.boxplot(list([range(0,100,5),range(10,50,5),range(0,50,4),range(30,45)]),showmeans=True)

#Customize plot
plt.title("Bar plot demo")
plt.xlabel("Datasets")
plt.ylabel("Range of values")
plt.grid(True)
plt.show()