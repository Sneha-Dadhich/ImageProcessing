import cv2
# opencv works on numpy library
import numpy as np


# read the image
img = cv2.imread(r"ImageProcessing\images\signature.jpg")
# flipping the image
# 0 means 180 degree, 1 means 360 degree
# 0 means flip by Vertical Axis and 1 means flip by Horizontal Axis
# -1 means flip by both vertical and horizontal axis
img_flip1 = cv2.flip(img, -1)
img_flip2 = cv2.flip(img, 0)
img_flip3 = cv2.flip(img, 1)

img_collection = np.hstack( (img_flip1, img_flip2, img_flip3) )
img_collection = cv2.resize(img_collection, (683,200))

cv2.imshow("Image reduced by half", img_collection)
cv2.waitKey(0)
