import cv2

# reading the image
img1 = cv2.imread(r"DRDO\images\leaf.jpg")

# displaying the original image
cv2.imshow("Original Image", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()



# propertion of downscaling 
downscale_pt = 40

# downscaling points 
height_down = int(img1.shape[0] * downscale_pt / 100)
wdth_down = int(img1.shape[1] * downscale_pt / 100)
dimension_down = (wdth_down, height_down)

image_resize_down = cv2.resize(img1, dimension_down)

cv2.imshow("Downscaled Images", image_resize_down)
cv2.waitKey(0)
cv2.destroyAllWindows()


# downscaling the image by recommended method for downscaling - cv2.INTER_AREA
image_resize_down2 = cv2.resize(img1, dimension_down, interpolation = cv2.INTER_AREA)
cv2.imshow("Downscaled Images By Recommended Method ( cv2.INTER_AREA )", image_resize_down2)
cv2.waitKey(0)
cv2.destroyAllWindows()


# propertion of upscaling 
upscale_pt = 300

# upscaling points 
height_down2 = int(img1.shape[0] * upscale_pt / 100)
wdth_down2 = int(img1.shape[1] * upscale_pt / 100)
dimension_up = (wdth_down2, height_down2)

image_resize_up = cv2.resize(img1, dimension_up)

cv2.imshow("Upscaled Images", image_resize_up)
cv2.waitKey(0)
cv2.destroyAllWindows()


# downscaling the image by recommended method for upscaling - cv2.INTER_CUBIC
image_resize_up2 = cv2.resize(img1, dimension_up, interpolation = cv2.INTER_CUBIC)
cv2.imshow("Upscaled Images By Recommended Method ( cv2.INTER_CUBIC )", image_resize_up2)
cv2.waitKey(0)
cv2.destroyAllWindows()