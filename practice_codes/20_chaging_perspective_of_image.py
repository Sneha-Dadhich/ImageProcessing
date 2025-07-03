import cv2
import numpy as np

# read the image
img1 = cv2.imread(r"DRDO\images\leaf.jpg")

# check if image is read properly
if img1 is None:
    print("Image not found. Please check the path.")
    exit()

# define 4 points in the original image (source points)
src_points = np.float32([[50, 50], [200, 50], [50, 200], [200, 200]])

# define 4 points where the source points should map to (destination points)
dst_points = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

# compute the perspective transform matrix
matrix = cv2.getPerspectiveTransform(src_points, dst_points)

# apply perspective transformation
result = cv2.warpPerspective(img1, matrix, (300, 300))

# display result
cv2.imshow("Perspective Transformed", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
