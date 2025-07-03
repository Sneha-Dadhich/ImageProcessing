import cv2
import os
from PIL import Image # PIL stands for Python Image Library
import numpy as np

# creating an object for face recognizer
face_R =  cv2.face.LBPHFaceRecognizer_create() # LBPH stands for  Local Binary Pattern Histogram.
# parameters taken by .LBPHFaceRecognizer_create()
# radius  # used to make circular patter
# neighbour # sample points to build the pattern
# gridx # cells in x axis
# gridy # cells in y axis
# threshold

face_D = cv2.CascadeClassifier(r"DRDO\codes\face_detection_model\haarcascade_frontalface_default.xml")

def learnLabels( path ):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    facepictures = []
    Ids = []

    for image in imagePaths:
        pilimage = Image.open(image).convert('L')
        imgarray_np = np.array(pilimage, 'uint8')
        Id = int(os.path.split(image)[-1].split(".")[1])
        faces = face_D.detectMultiScale(imgarray_np)

        for (x, y, w, h) in faces:
            facepictures.append(imgarray_np[ y:y+h, x:x+w])
            Ids.append(Id)
        
    return facepictures, Ids

faces, Ids = learnLabels( r"DRDO\codes\face_detection_model\dataset")
face_R.train(faces, np.array(Ids))
face_R.save(r"DRDO\codes\face_detection_model\model\model.yml")