'''This program will read an image file and display the matrix
You need to install opencv-python for this to work $pip install opencv-python
Each image is returned as numpy arrary by opencv-python
 Notice that color image will have 3-D matrix where as grayscale image will have 2-D matrix'''

import cv2

colorImage = cv2.imread("../resources/roses.jpg",1) #Read the image in RGB color format. 2nd parameter flag 1 indicates color image
print(type(colorImage))  #Notice that image is returned as Numpy array
print('Displaying color image matrix (3D)')
print(colorImage)

bwImage = cv2.imread("../resources/roses.jpg",0)  #Read the image as grayscale or black&white image. 2nd parameter flat 0 indicates back&white image
print('Displaying black and white image matrix (2d)')
print(bwImage)

#Some other functions of opencv
print("Color image size = "+str(colorImage.shape)+ " Black&White image size = "+str(bwImage.shape)) #See that color image has 3 channels and grayscale image has 2 channels
