import cv2

img1 = cv2.imread(r"DRDO\images\leaf.jpg")
img2 = cv2.imread(r"DRDO\images\leaf3.jpg")
img3 = cv2.imread(r"DRDO\images\leaf8.jpg")
greyscale_img = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)

# resizing the image to be added
img1 = cv2.resize(img1, (500, 500))
img2 = cv2.resize(img2, (500, 500))
greyscale_img = cv2.resize(greyscale_img, (500, 500))


# creating the mask
retval, mask = cv2.threshold(greyscale_img, 150, 255, cv2.THRESH_BINARY)
retval2, mask2 = cv2.threshold(greyscale_img, 150, 255, cv2.THRESH_BINARY_INV)

# adding the image with mask
added_image = cv2.add(img1, img2, mask=mask)
added_image2 = cv2.add(img1, img2, mask=mask2)

cv2.imshow("Combined Image with  Mask", added_image)
cv2.imshow("Combined Image with Inverted Mask", added_image2)

cv2.waitKey(0)
cv2.destroyAllWindows()