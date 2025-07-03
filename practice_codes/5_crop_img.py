import cv2
# opencv works on numpy library
import numpy as np


# read the image
img = cv2.imread(r"ImageProcessing\images\wallpaper.jpg")
img = cv2.resize(img, (500, 600))

# cropping from top ['height axis', 'width axis']
img_crop1 = img[0:100, 0:100]
cv2.imshow("Original Image", img)
cv2.imshow("Cropping the image from top side", img_crop1)
cv2.waitKey(0)
