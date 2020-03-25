import datetime as dt
import numpy as np
import cv2 as cv2;

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")


def faceDetect(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    return faces


def eyeDetect(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray, 1.1, 4)
    return eyes


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
print(cap.get(3))
print(cap.get(4))

fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
out = cv2.VideoWriter("output.avi", fourcc, 30, (640, 480))

font = cv2.FONT_HERSHEY_COMPLEX

number = 9
sec = 0
while cap.isOpened():
    number += 1
    if number % 30 == 0:
        sec += 1
    ret, frame = cap.read()
    height, width, channels = frame.shape

    dateAndTime = dt.datetime.now()
    frame = cv2.putText(frame, str(dateAndTime), (0, height - 1), font, 1, (255, 255, 255), 2)
    frame = cv2.putText(frame, str(sec), (width - 50, height), font, 1, (255, 255, 255), 2)

    if number % 10 == 0:
        faces = faceDetect(frame)
    for i in faces:
        if number % 10 == 0:
            imCrop = frame[i[1] : int((i[1] + i[3]) * 0.7) , i[0] : (i[0] + i[2])]
            eyes = eyeDetect(imCrop)
        for j in eyes:
            print("j = ", j)
            cv2.rectangle(frame, (i[0] + j[0], i[1] + j[1]), (i[0] + j[0] + j[2], i[1] + j[1] + j[3]), (0, 255, 255), 1)
        cv2.rectangle(frame, (i[0], i[1]), (i[0] + i[2], i[1] + i[3]), (255, 255, 255), 2)
    if ret:
        out.write(frame)
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
out.release()
cv2.destroyAllWindows()
