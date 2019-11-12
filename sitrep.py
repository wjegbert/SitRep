# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 19:56:24 2019

@author: William
"""

import cv2
import winsound

goal = 25
n = 0
cv2.VideoCapture(0).release
HAARPATH = "haarcascades/haarcascade_frontalface_default.xml"
cap=cv2.VideoCapture(0)
face_detect=cv2.CascadeClassifier(HAARPATH)

faces =[]
prevface = []
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if n>=goal:
        break
    # Our operations on the frame come here
    if ret is True:
        prevface = faces
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces=face_detect.detectMultiScale(gray, 1.3, 7)
        if len(faces) > 0 and len(prevface) == 0: 
            n = n+1
            winsound.MessageBeep(winsound.MB_ICONHAND)
            print (n)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

            
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print ("\a")
cap.release()
cv2.destroyAllWindows()
