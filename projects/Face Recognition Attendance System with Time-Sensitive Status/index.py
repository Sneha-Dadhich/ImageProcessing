import cv2
import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import numpy as np
import pandas as pd
import csv
from attendence import check_attendance

# Load models
face_R = cv2.face.LBPHFaceRecognizer_create()
face_R.read(r"DRDO\codes\face_detection_model\model\model.yml")

face_D = cv2.CascadeClassifier(r"DRDO\codes\face_detection_model\haarcascade_frontalface_default.xml")
eye_D = cv2.CascadeClassifier(r"DRDO\codes\face_detection_model\haarcascade_eye.xml")

is_recognition_active = False
last_logged_id = None  # To avoid duplicate logs


def add_data(row, filename):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)
    
    registration_data = pd.read_csv(r"DRDO\codes\Face Recognition Attendance System with Time-Sensitive Status\user_registration.csv")
    attendance_log_data = pd.read_csv(r"DRDO\codes\Face Recognition Attendance System with Time-Sensitive Status\Attendence_log.csv")

    



def update_frame():
    global cam, is_recognition_active, last_logged_id
    ret, frame = cam.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_D.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

            # Eye detection
            eyes = eye_D.detectMultiScale(roi_color)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
           
            if is_recognition_active:
                Id, conf = face_R.predict(roi_gray)
                if conf > 50:
                    name = "Unknown"
                    if Id == 1:
                        name = "Sneha"
                    elif Id == 2:
                        name = "Simi"
                    
                    cv2.putText(frame, f"{name} ({conf:.2f})", (x, y-10),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
                    
                    # Only log once per person
                    if last_logged_id != Id:
                        login_time, date, status = check_attendance()
                        data = [Id, name, login_time, date, status]
                        add_data(data, r"DRDO\codes\Face Recognition Attendance System with Time-Sensitive Status\Attendence_log.csv")
                        last_logged_id = Id  # Prevent logging again immediately

                else:
                    cv2.putText(frame, "Not Registered", (x, y-10),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Convert to RGB for Tkinter
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        lbl.imgtk = imgtk
        lbl.configure(image=imgtk)

    lbl.after(10, update_frame)

def start_camera():
    global cam
    cam = cv2.VideoCapture(0)
    update_frame()

def toggle_recognition():
    global is_recognition_active, last_logged_id
    is_recognition_active = not is_recognition_active
    last_logged_id = None  # Reset to allow fresh logging
    login_btn.configure(text="Stop Recognition" if is_recognition_active else "Start Recognition")

def close_app():
    if cam:
        cam.release()
    root.destroy()

# Initialize GUI
root = tk.Tk()
root.title("Face Recognition App")
root.geometry("800x600")

lbl = Label(root)
lbl.pack()

btn_start = tk.Button(root, text="Start Camera", command=start_camera,
                      font=('Arial', 14), bg="green", fg="white")
btn_start.pack(pady=10)

login_btn = tk.Button(root, text="Start Recognition", command=toggle_recognition,
                      font=('Arial', 14), bg="blue", fg="white")
login_btn.pack(pady=10)

btn_exit = tk.Button(root, text="Exit", command=close_app,
                     font=('Arial', 14), bg="red", fg="white")
btn_exit.pack(pady=10)

cam = None

root.mainloop()
