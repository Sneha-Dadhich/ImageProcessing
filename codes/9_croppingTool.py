import cv2
# opencv works on numpy library
import numpy as np


# read the image
img = cv2.imread(r"ImageProcessing\images\wallpaper.jpg")

# making the cropping tool using event handling
drawing = False
ix = -1
iy = -1

def draw(event,x,y,flags,params):    
    
    global drawing, ix, iy
    
    if event == 1:
        print("Mouse-Clicked : Start Drawing")
        drawing = True
        ix = x
        iy = y    

    elif event == 0 and drawing == True:
        print("Mouse-Draging : Start Drawing")        
        # cv2.rectangle(img_created3, pt1=(ix,iy), pt2=(x,y), color=(0,0,255), thickness=2)

    elif event == 4:
        drawing = False
        # saving the cropped image
        img_copy = img.copy()
        cv2.rectangle(img, pt1=(ix,iy), pt2=(x,y), color=(0,0,255), thickness=2)
        

        # it is img[height, width]
        save_image = img_copy[min(iy-1, y-1):max(iy-1, y-1), min(ix-1, x-1):max(ix-1, x-1)]
        cv2.imwrite(r".\ImageProcessing\Cropped_image.jpg", save_image)
        cv2.imshow("Saving the image", save_image)


cv2.namedWindow(winname="Crop the window")
cv2.setMouseCallback("Crop the window", draw)

while True:
    cv2.imshow("Crop the window", img)
    
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

# destroy all the windows
cv2.destroyAllWindows()
