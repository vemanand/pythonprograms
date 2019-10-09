''' This program will read an image and show it
Before displaying the image, we will write something on the image - A Line, Rectangle, Circle, Polygon and Text'''

import cv2
import numpy as np

img = cv2.imread("../resources/roses.jpg",cv2.IMREAD_COLOR)

#Draw line using line(source, <line start>,<line beginning>,<color in BGR>,<optional line width>)
cv2.line(img,(5,25),(150,250),(0,0,255),15)  #Draws Redline with 15 thickness

#Draw rectangle using rectangle(<source>,<top left coordinates>,<bottom right coordinates>, <BGR Color>,<optional line thickness>)
cv2.rectangle(img, (50,50),(250,250),(255,0,0),5)

#Draw circle using circle(<source>,<center coordinate>,<radius>,<BGR color>,<optional thickness>). Negative line thickness will fill the circle/shape
cv2.circle(img,(300,350),100,(0,255,0),-1)

#Draw a polygon. This will have a number of points which are connected and optionally closed to form a polygon
points = np.array([[250,50],[300,100],[300,200],[200,300],[100,200]])

#Draw the shape using polylines(<source>,<points coordinates>,<close or not>,<BGR Color>,<Optional thickness>)
cv2.polylines(img,[points],True,(100,10,200),3)

#Write some Text using putText (source,"<text/message>",<position>,<font face>,<font scale>,<BGR Color>,<width>)
font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(img,"OpenCV Tutorials",(10,500),font,1,(30,55,10),3)

cv2.imshow("Image with drawings",img)
cv2.waitKey(0)
cv2.destroyAllWindows()