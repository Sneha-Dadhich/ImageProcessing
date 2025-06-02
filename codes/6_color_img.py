import cv2
# opencv works on numpy library
import numpy as np


# read the image
img = cv2.imread(r"ImageProcessing\images\wallpaper.jpg")
 # # saving the image
# converting the image to only Blue, Green, Red
img_saved1, img_saved2, img_saved3= img.copy(), img.copy(), img.copy()
img_saved1[:,:, 0] = 0
img_saved2[:,:, 1] = 0
img_saved3[:,:, 2] = 0
img_saved4 = np.hstack( (img_saved1, img_saved2, img_saved3) )
cv2.imwrite(r".\ImageProcessing\Saved_Blue_Img88.jpg", img_saved2)
cv2.imshow("Saving the image", img_saved4)
cv2.waitKey(0)
