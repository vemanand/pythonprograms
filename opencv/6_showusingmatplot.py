'''#This program will read an image and display the same using pyplot imshow method - Not using cv2.imshow()
This will also store/save the image to another file using OpenCV "imwrite" method
'''

import cv2
from matplotlib import pyplot as plt

#Read file using imread. Optionally you can read in grascale
img = cv2.imread('../resources/roses.jpg',cv2.IMREAD_GRAYSCALE)
#img = cv2.imread('../resources/roses.jpg',1)

#Display the image using pyplot and hide X-axis, Y-axis values
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # Hide tick values on X and Y axis

#Optionally - You can plot a line on the image
plt.plot([200,300,400],[100,200,300],'c', linewidth=5)

#Display the image. Optionally you can give a title
plt.title("Read image from OpenCV and display using MatPlot")
plt.show()

#Optionally you can save the image using "imwrite" by giving destination file name and source image.
cv2.imwrite("../output/gray_roses.jpg",img)