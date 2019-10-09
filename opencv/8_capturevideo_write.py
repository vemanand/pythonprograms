''' This program will capture the video and save the recording to a file
We create a Video Codec using which we want to record the video. Create VideoWriter using this codec
Use the "write" method to continuously write frames untul the user press the key "q" '''

import cv2

#Capture video from your webcam
cap = cv2.VideoCapture(0)

#You could also load from a video file, if you want
#cap = cv2.VideoCapture("../resources/30secs_intro.mp4")

#Create a video Codec
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#Create video writer object using the above Codec. Give the filename you want to write to and the video size
outfile = cv2.VideoWriter('../output/captured_video.avi', fourcc, 20.0, (640,480))

#Continue capturing video, show in the window and write to the file
#Until the user press 'q' button on the keyboard
while True:
    ret, frame = cap.read()
    outfile.write(frame)
    cv2.imshow('Your webcam',frame)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

#Release all resources
cap.release()
outfile.release()
cv2.destroyAllWindows()