import cv2
import numpy as np

# read the image
img = cv2.imread(r"DRDO\images\wallpaper.jpg")
# flipping the image
# 0 means 180 degree, 1 means 360 degree
# 0 means flip by Vertical Axis and 1 means flip by Horizontal Axis
# -1 means flip by both vertical and horizontal axis
img_flip1 = cv2.flip(img, -1)
img_flip2 = cv2.flip(img, 0)
img_flip3 = cv2.flip(img, 1)


# showing all the images in one window
img_collection = np.hstack( (img_flip1, img_flip2, img_flip3) )
img_collection = cv2.resize(img_collection, (683,200))
cv2.imshow("Image reduced by half", img_collection)
cv2.waitKey(0)
cv2.destroyAllWindows()

# rotating the image
rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
rotated_img2 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow("Image Rotated by 90", rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Image Rotated by 90 (Anti-clockwise)", rotated_img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# rotate by any degree
# finding the center of the image
(h, w) = img.shape[:2]
image_centre = (w // 2, h // 2)
print(f"Coordinates of Image Centre : {image_centre}")

rotation_matrix = cv2.getRotationMatrix2D( image_centre, 145, 1.0)
rotated_img3 = cv2.warpAffine( img, rotation_matrix, (500, 500), flags = cv2.INTER_LINEAR)

cv2.imshow("Rotated Image BY 45 DEGREE", rotated_img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
