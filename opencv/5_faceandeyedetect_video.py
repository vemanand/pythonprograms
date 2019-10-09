import cv2

face_cascade = cv2.CascadeClassifier('../resources/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('../resources/haarcascade_eye.xml')

vid = cv2.VideoCapture(0)
while True:
    ret, img = vid.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        #roi_gray = gray[y:y+h, x:x+w] #This may detect your mouth also as eye
        roi_gray = gray[y:y-int((y + h) * 0.7), x:x + w] #Try to consider ROI as just upper 70% of the face image to avoid mouth detection
        roi_color = img[y:y-int((y + h) * 0.7), x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,10), 1)

    cv2.imshow('My Image',img)
    #Wait for key and exit on Esc key
    key = cv2.waitKey(30) & 0xff
    if key == 27:
        break

#Relese the camera
vid.release()
cv2.destroyAllWindows()