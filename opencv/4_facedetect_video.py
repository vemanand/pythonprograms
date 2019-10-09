import cv2

face_cascade = cv2.CascadeClassifier('../resources/haarcascade_frontalface_default.xml')

vid = cv2.VideoCapture(0)
while True:
    ret, img = vid.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
    cv2.imshow('My Image',img)
    key = cv2.waitKey(30) & 0xff
    if key == 27:
        break

vid.release()
cv2.destroyAllWindow()
