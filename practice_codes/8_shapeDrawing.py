import cv2
import numpy as np
import random
# opencv works on numpy library


# read the image
img = cv2.imread(r"ImageProcessing\images\wallpaper.jpg")

# making the colour selector
rand_color_selection = random.randint(0, 255)
#  --- Complex Even Handling ---
# making the square using event handling
drawing = False
ix = -1
iy = -1

# ye parameter daalne jaroorri hai
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
        cv2.rectangle(img_created3, pt1=(ix,iy), pt2=(x,y), color=(0,0,255), thickness=2)

cv2.namedWindow(winname="Complex_Event_Handling")
cv2.setMouseCallback("Complex_Event_Handling", draw)

img_created3 = img = np.zeros( (512, 512, 3))

while True:
    cv2.imshow("Complex_Event_Handling", img_created3)
    
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

# destroy all the windows
cv2.destroyAllWindows()
