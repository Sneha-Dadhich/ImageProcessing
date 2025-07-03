
import cv2
image = cv2.imread(r"C:\Users\Dell\Desktop\Sneha2.0\Programs1\Python\DRDO\images\bg2.jpg")
# splitting the colour channel 
blue_channel, green_channel, red_channel = cv2.split(image)
# cv2.imshow('Blue Channel', blue_channel)
# cv2.imshow('Green Channel', green_channel)
# cv2.imshow('Red Channel', red_channel)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

merged_image = cv2.merge([red_channel ,green_channel, blue_channel ]) # RGB channel
merged_image2 = cv2.merge([blue_channel ,green_channel, red_channel ]) # RGM channel
cv2.imshow("Merged_image", merged_image)
cv2.imshow("Merged_image 2 ", merged_image2)

cv2.waitKey(0)
cv2.destroyAllWindows()
