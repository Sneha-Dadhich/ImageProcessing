import cv2
# opencv works on numpy library
import numpy as np

# read the image
img = cv2.imread(r"ImageProcessing\images\wallpaper.jpg")
# resizing the image
img_resize = cv2.resize(img, (800,800))
cv2.imshow("Image Resized", img_resize)
cv2.waitKey(0)

# decreasing the images to half of its original size
img_half = cv2.resize(img, (img.shape[0]//2, img.shape[1]//2) )
cv2.imshow("Image reduced by half", img_half)
cv2.imshow("Original Image", img)
cv2.waitKey(0)
