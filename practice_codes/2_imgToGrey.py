import cv2
import numpy as np


# read the image
img = cv2.imread(r"ImageProcessing\images\wallpaper.jpg")
# converting image in grayscale image
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("window", img_gray)
cv2.waitKey(0) 
