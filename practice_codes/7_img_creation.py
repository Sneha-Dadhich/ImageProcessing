import cv2
# opencv works on numpy library
import numpy as np


# read the image
img = cv2.imread(r".\signature.jpg")

# creating your own image
# creating an black window
img_created = img = np.zeros( (512, 512, 3))
# creating a rectangle in the created black window
cv2.rectangle(img_created, pt1=(100,100), pt2=(300,300), color=(255,0,0), thickness=3)
# creating a rectangle in the created black window with color filled in it
cv2.rectangle(img_created, pt1=(150,150), pt2=(300,300), color=(255,0,0), thickness=-100)
# creating a circle in the created black window
cv2.circle(img_created, center=(225,225), radius=50, color=(0,255,255), thickness=2)
# creating a circle in the created black window with color filled in it
cv2.circle(img_created, center=(225,225), radius=20, color=(0,255,255), thickness=-1)
# creating a line in the created black window
cv2.line(img_created, pt1=(100, 100), pt2=(150, 150), color=(0,0,255), thickness=3)
# inserting the image in the window
cv2.putText(img_created, org=(100, 400), fontScale=1, color=(255,0,255), thickness = 2, lineType=cv2.LINE_AA, text="This is my first text", fontFace=cv2.FONT_HERSHEY_TRIPLEX)
cv2.imshow("Created Image1", img_created)
cv2.waitKey(0)
