import cv2

'''
This program will load an  image and detect faces within it. We use haarcascades XML file where the features are stored
You should be able to find haarcascades for various items/things by searching on the internet
haarcascades are available on Github (search for Haarcascades Github): https://github.com/opencv/opencv/tree/master/data/haarcascades
'''

#Craeate a Cascadeclassifier object using harrcascade
face_cascade = cv2.CascadeClassifier("../resources/haarcascade_frontalface_default.xml")

#Read the image in which you want to detect the faces
img = cv2.imread("../resources/myphoto.jpg")

#Convert the image as grayscale image to improve face detection. It is standard practice to convert image to grayscale for any analysis purposes
bw_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Search for the coordinates of the faces in the image by applying face_cascade. This will help detect the coordinates of the face(s) in the image
faces = face_cascade.detectMultiScale(bw_img, scaleFactor=1.05, minNeighbors=5)
print(type(faces))

#Optionally you can show image before processing
cv2.imshow("Original image - before process",img)
#Process the image to add rectangular boxes around each face (coordinates) detected above.
# first coordinate is the image in which you want to detect, 2nd and 3rd are the width and height of the rectangle
# 0,255,0 is the RGB color of the rectangle. Change this to get different color. 3 is line width;
for (x,y,w,h) in faces:
    img = cv2.rectangle(img, (x,y), (x+w, y+h),(0,255,0), 3) #You don't need to store the image as well as shown in next example below
#Show image in the window
cv2.imshow("Original Image - After process",img)


#Use below code instead when the orginal image is big and you want to resize it, before processing
img = cv2.imread("../resources/withson.jpg")
#Resizing the image to 1/4th size. Change this based on your image size
img_resized = cv2.resize(img, (int(img.shape[1]/4), int(img.shape[0]/4)))
bw_img = cv2.cvtColor(img_resized,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(bw_img, scaleFactor=1.05, minNeighbors=5)
for (x,y,w,h) in faces:
    cv2.rectangle(img_resized, (x,y), (x+w, y+h),(255,0,0), 3)  #Not storing the return type
cv2.imshow("Resized Image -Face detect",img_resized)


#Common code to wait for a key and destroy all windows
cv2.waitKey(0)
cv2.destroyAllWindows()