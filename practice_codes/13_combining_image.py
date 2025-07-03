import cv2
import numpy as np

image = cv2.imread(r"DRDO\images\wallpaper.jpg")
image2 = cv2.imread(r"DRDO\images\bg1.jpg")

# changing the dimensions of the image
image = cv2.resize(image,(600,600))
image2 = cv2.resize(image2,(600,600))

# take images of same dimensions (hame width, height and channel) to combine them
added_image = cv2.add(image2, image)
print(added_image.shape)
# cv2.imshow("Combined Image",added_image)

# adding the image via weight
added_image2  = cv2.addWeighted(image, 0.25, image2, 1.0, 10)

cv2.imshow("Combined Image Via Weight",added_image2)
cv2.waitKey(0)
cv2.destroyAllWindows()