import cv2
# opencv works on numpy library
import numpy as np


# read the image
img = cv2.imread(r"ImageProcessing\images\wallpaper.jpg")
# printing image info
print(f"Image Info :\n {"."*5} Image Array {"."*5}")
print(f"{img}")
print(f"Image Type : {type(img)}")
print(f"Image Shape :{img.shape}")
print(f"Number of rows and columns in image (length x width) : {img.shape[:2]}")
print(f"Number of channels : {img.shape[2]} \t # Here it follows RGB pattern hence has 3 channels")


# displaying all three images at once
cv2.imshow("Coloured Images", img)
cv2.waitKey(0) 
