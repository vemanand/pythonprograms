''' This program will capture the video and displays the same
We use "VideoCapture" to start capturing video and read() method to read frames. We convert the frame to grayscale (black & white)
Will continuourly loop through and display the frames, until the user press "q" on the keyboard
We will display both the original video and processed video (apply different colors, filters etc to original one)'''

import cv2

# Use VideoCapture method to start capturing video
# The parameter value is the camera number: 0 for built-in camera, 1 for external camera and so on
video = cv2.VideoCapture(0)

#Read video - returns two values. One boolean true/false to check if the video is captured or not (read is successful or not).
# Another value that returns the frames which is a numpy array
#check,frame = video.read()


#Optional variable to capture the number of frames, in case you want to capture
frames = 0

#We want to display all the frames as long s check=true (video is being captured). We will use while loop to accomplish this
#The loop will continue until the user press the key 'q'
while True:
    frames += 1  #Increment the number of frames
    check, frame = video.read()

    #Optionally you can convert the frame to gray scale and display
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #Display the original frame and grascale frame
    cv2.imshow("Actual video", frame)
    cv2.imshow("Grayscale video", gray)

    #Capture key and Quit the loop when the user types q
    key = cv2.waitKey(1) #Wait for 1 milli second. This means, a new frame is captured for every milli second
    if key == ord('q'):  #To avoid variable declaration you can also write if cv2.waitKey(1) && 0xFF == ord('q'):
        break

print("Number of frames = "+str(frames))
#Release the camera and close window
video.release()
cv2.destroyAllWindows()