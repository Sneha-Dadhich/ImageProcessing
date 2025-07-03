import cv2
from PIL import Image
import numpy as np

# importing the image via PIL
pil_image = Image.open(r"C:\Users\Dell\Desktop\Sneha2.0\Programs1\Python\DRDO\images\bg2.jpg")
# CONVERTING THE IMAGE IN NPARRAY
pil_image_array = np.array(pil_image)
print(f"pil_image_array : \n{pil_image_array}")

# pil_image.show()

