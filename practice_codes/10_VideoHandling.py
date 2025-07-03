import cv2
# opencv works on numpy library
import numpy as np


# read the image
img = cv2.imread(r"ImageProcessing\images\wallpaper.jpg")

# handling videos using opencv
# capturing video by webcam 

cap = cv2.VideoCapture(0)
# fetching the exat dimenrsions of webcam
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# saving the image
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(r"./SavedVideo4.avi", fourcc,20.00, (frame_width, frame_height))

while True:
    ret, frame = cap.read()
    
    img_edited = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    out.write(img_edited)

    cv2.imshow("webcam", frame)
    print(ret)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

