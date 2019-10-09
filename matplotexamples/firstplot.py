'''
Document reference: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
Sample program to draw Line chart
'''
import numpy as np
import matplotlib.pyplot as plt

#Define sample dataset
xval = np.arange(0,10,1)
yval = 2*xval + 5

#Plot datapoints
'''Possible marker values: https://matplotlib.org/3.1.1/api/markers_api.html#module-matplotlib.markers  Ex: 1,2,3,4,8,alphabet o, <, >, letter v, carrot ^,s,+,x, X, d,D,
#linestyle or ls values: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linestyle Ex: 'solid', 'dashed', 'dashdot'
#color or c values: https://matplotlib.org/3.1.1/api/colors_api.html?highlight=color%20values Ex: b or g or c or m or y or k or w. blue or orange or purple or brown or cyan
we can use RGB colors '#0f0f0f' or '#0f1b2c' OR RGBA float values as tuple (0.1,0.2,0.4) or (0.2,0.3,0.6,0.8) OR Tableau colors 'tab:pink' or 'tab:green' or 'tab:red' etc
'''
plt.plot(xval,yval,linewidth=2.0,linestyle=":",color="blue",alpha=0.7,marker='*')
plt.title("Line chart sample")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend(['Linear Equation'],loc='best')
plt.grid(True)
plt.show()
