import cv2
import numpy as np

image = cv2.imread(r"DRDO\images\bitwise.jpg")
image2 = cv2.imread(r"DRDO\images\bitwise2.jpg")

# changing the dimensions of the image
image = cv2.resize(image,(600,600))
image2 = cv2.resize(image2,(600,600))

#bitwise 'and' operation
bit_add_img = cv2.bitwise_and(image, image2)
# cv2.imshow("Bitwise Added Image", bit_add_img)

#bitwise 'or' operation
bit_add_img2 = cv2.bitwise_or(image, image2)
cv2.imshow("Bitwise 'Or' Image", bit_add_img2)

#bitwise 'xor' operation ie convert black to white and white to black
bit_add_img3 = cv2.bitwise_xor(image, image2)
cv2.imshow("Bitwise 'Or' Image", bit_add_img3)

cv2.waitKey(0)
cv2.destroyAllWindows()