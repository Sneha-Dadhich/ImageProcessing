import cv2
import numpy as np

# reading the image
img1 = cv2.imread(r"DRDO\images\leaf.jpg")

height, width = img1.shape[:2]

transformation_matrix = np.float32([ [1, 0, 100], [0, 1, 40] ]) # there will be 0 on img1[0:100] and img1[1:40]
transformation_matrix2 = np.float32([ [1, 0, -100], [0, 1, -40] ])

transformation_image = cv2.warpAffine( img1, transformation_matrix, (width, height))
transformation_image2 = cv2.warpAffine( img1, transformation_matrix2, (width, height))

print(f"Original Image Resolution (Width, Height) : {img1.shape}")
print(f"Transformed Image Resolution (Width, Height) : {transformation_image.shape}")

cv2.imshow("Transformed Image (Top Left)", transformation_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Transformed Image (Bottom Right)", transformation_image2)
cv2.waitKey(0)
cv2.destroyAllWindows()