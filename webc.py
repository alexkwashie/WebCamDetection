import cv2, time

#get webcam images, 0 - webcam, 1- for anyother cam
video = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

a = 1

while True:
    a = a+1

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

print(a, " frames")
#show video window
video.release()
cv2.destroyAllWindows()

