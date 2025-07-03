import cv2
import numpy as np
import os
import time

# making the dataset
face = cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")
cam = cv2.VideoCapture(0)

# registration of user
id = input(" Please enter your id : ")
name = input("Please enter you name : ")

# picture is the image in the dataset folder
picture = 0
while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 5)

    for (x, y, w, h) in faces:
        picture = picture + 1
        # this takes only the area consisting of face from the image storing in the dataset folder
        cv2.imwrite(fr"dataset\user.{str(id)}.{str(id)}.{str(picture)}.{str(name)}.jpg", gray[y:y+h, x:x+w]) 
        cv2.rectangle(img, (x, y), (x + w, y + h), (0,255,0), 2)
    cv2.imshow("Registration", img)
    cv2.waitKey(50) # capturing the image in every 50 seconds

    if ( picture > 300 ):
        break

cam.release()
print(f"{'*' * 6} Registration Sucessfull {'*' * 6}")
