import cv2

img_for_mask = cv2.imread(r"DRDO\images\mask1.png")
img1 = cv2.imread(r"DRDO\images\wallpaper.jpg")
img2 = cv2.imread(r"DRDO\images\bg1.jpg")

# converting the image used for greyscale to greyscale
circle_grayscale = cv2.cvtColor(img_for_mask, cv2.COLOR_BGR2GRAY)

# resizing the image to be added
img1 = cv2.resize(img1, (500, 500))
img2 = cv2.resize(img2, (500, 500))
circle_grayscale = cv2.resize(circle_grayscale, (500, 500))

# creating a mask
retval , mask = cv2.threshold(circle_grayscale, 10, 255, cv2.THRESH_BINARY)
# inverting the mask
retval2 , mask2 = cv2.threshold(circle_grayscale, 10, 255, cv2.THRESH_BINARY_INV)

# making an inverted mask
inv_mask = cv2.bitwise_not(mask)

# Adding the img1 and img2
added_image = cv2.add(img1, img2, mask = mask)
added_image2 = cv2.add(img1, img2, mask = mask2)

cv2.imshow("Combined Image with Mask", added_image)
cv2.imshow("Combined Image with Inverted Mask", added_image2)

cv2.waitKey(0)
cv2.destroyAllWindows()