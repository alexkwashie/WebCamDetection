import cv2, time

#get webcam images, 0 - webcam, 1- for anyother cam
video = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    check, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #add a face search area size
    faces = face_cascade.detectMultiScale(gray,
    scaleFactor = 1.05,
    minNeighbors = 7)

    #draw face detected area
    for x, y, w, h in faces:
        img=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,225,0),2)

    print(check)
    print(frame)

    #time.sleep(0)
    cv2.imshow('capture', frame)

    key = cv2.waitKey(1)

    #Close window
    if key == ord('q'):
        break

#show video window
video.release()
cv2.destroyAllWindows()

'''
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()'''