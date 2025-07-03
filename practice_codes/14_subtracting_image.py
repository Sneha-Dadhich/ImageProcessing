import cv2
import numpy as np

image = cv2.imread(r"DRDO\images\wallpaper.jpg")
image2 = cv2.imread(r"DRDO\images\bg1.jpg")


# changing the dimensions of the image
image = cv2.resize(image,(600,600))
image2 = cv2.resize(image2,(600,600))

# order of the image is important as it is not commutative
subtracted_image = cv2.subtract(image, image2)
cv2.imshow("Subtracted Image", subtracted_image)

cv2.waitKey(0)
cv2.destroyAllWindows()