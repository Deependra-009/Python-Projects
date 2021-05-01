import cv2 as cv
webcam = cv.VideoCapture(0)
cascade = cv.CascadeClassifier("face_detection.xml")

while True:
    st, img = webcam.read()
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(
        gray,                               # the b/w image
        scaleFactor = 1.1,                   # adjust the face near and far from camera
        minNeighbors = 5,                   # for the algo to find face relative to other items
        minSize=(30,30),                    # min box size

    )
    if len(faces) > 0:
        for (x,y,w,h) in faces:
            cv.rectangle(img,(x,y),(x+w,h+y),(0,255,0),2)

    cv.imshow('normal image',img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv.destroyAllWindows()