"""This program will read and display an image in a window
First we will read and display orignial image
Next we will convert the image to grascale and display. Close all windows
Next resize the image in 2 days (custom and symmetric) and display
waitKey method is used to exit when the user press any key on the keyboard
"""

import cv2

#Read image as Color image - 2nd parameter is 1
img1 = cv2.imread("../resources/roses.jpg",1)

#Display the image in a window with some title
cv2.imshow("Color image",img1)
cv2.waitKey(0) #Will wait until the user press any (keyboard) key. You can specify timeline in milliseconds cv2.waitKey(2000)

#Read image as black & white image. For 2nd parameter Color is 1, Grayscale is 0 and the unchanged is -1
img2 = cv2.imread("../resources/roses.jpg",0)
cv2.imshow("Black and White image",img2)
cv2.waitKey(0)

#Close and destroy all the windows
cv2.destroyAllWindows()

#Resize the image to the given dimensions. Notice that the size to be given as Tuple. The image may not be symmetrical based on the given size
resized = cv2.resize(img1,(700,400))
cv2.imshow("Custom Resize",resized)

#Resize the image to make it half and display. For this divide the shape by 2 for each row, column and convert to int to provide in tuple
#You can also multiply by 2 to double the size
sym_resized = cv2.resize(img1,(int(img1.shape[1]/2),int(img1.shape[0]/2)))
cv2.imshow("Symmetric Resize",sym_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
#Uncomment this to see how we can get a pixel or update a pixel, region of the image
#You can read or update a pixel color
px = img1[155,160] #Will get the Pixel color at the given location
print(px)
img1[155,160] = [0,0,0] #Will change the Pixel color of the image to specified BGR color
#You can also access ROI - Region Of an Image and manipulate the color
roi =img1[100:150, 100:150]
print(roi)
#Update region of an image with different color
img1[100:150,100:250] = [255,255,255]  #Will convert given region to white color
#You can also copy regions of images (ROI) to another place
flowers = img1[100:200,150:200]  #Copy some region of flowers
img1[0:100, 0:50] = flowers  #Assign/paste the above region to a different region in the image
cv2.imshow("Updated ROI",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''