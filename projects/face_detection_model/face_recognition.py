import cv2
import numpy as np

def recognize():
    # load the LBPH classifier
    face_R = cv2.face.LBPHFaceRecognizer_create()
    # read the dataset
    face_R.read(r"model\model.yml")

    face_D = cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")
    # perform eyes detection
    eye = cv2.CascadeClassifier(r"haarcascade_eye.xml")

    # initialize the video capture
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX

    while 1:
        retention, image = cam.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_D.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5)

        for (x, y, w,h ) in faces:
            cv2.rectangle(image, (x,y), (x+w, y+h), (255, 0, 0), 3)
            region_of_interest_gray = gray[y:y+h, x:x+w]
            region_of_interest_color = image[y:y+h, x:x+w]
        
            # eyes detection
            eyes = eye.detectMultiScale(region_of_interest_color)
        
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(region_of_interest_color, (ex, ey), (ex+ew, ey+eh), (0,255,0), 3)

            # Recognition
            Id, conf = face_R.predict(gray[y:y+h, x:x+w])

            if (conf > 50):
                cv2.putText(image, "sucessfull", (x-50, y-50), font, 1, (255,255,0), 2)
            
                if (Id == 1):
                    Id = "Sneha"
                elif (Id == 2):
                    Id = "Simi" 
        
            else:
                Id = "NOT REGISTERED"
                cv2.putText(image, "Not Successfull", (x-50, y-50), font, (255,255,255), 3)

            cv2.putText(image, str(Id), (x+10, y), font, 1 , (255,0,255), 2)
            cv2.putText(image, str(conf), (x+10, y-100), font, 1 , (255,0,255), 2)

        cv2.imshow("Face Recognition", image)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
            break

    # return image        
    cam.release()
    cv2.destroyAllWindows()

    return cam

recognize()