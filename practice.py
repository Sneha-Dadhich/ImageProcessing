import cv2
# opencv works on numpy library
import numpy as np


# read the image
img = cv2.imread(r".\signature.jpg")
# printing image info
print(f"Image Info :\n {"."*5} Image Array {"."*5}")
print(f"{img}")
print(f"Image Type : {type(img)}")
print(f"Image Shape :{img.shape}")
print(f"Number of rows and columns in image (length x width) : {img.shape[:2]}")
print(f"Number of channels : {img.shape[2]} \t # Here it follows RGB pattern hence has 3 channels")

# # opencv follws Blue, Green, Red instead of Red, Green, Blue
# # manipulating the Blue/Green/Red (color channels) of image
# imgBlue = img[:,:,0]
# imgGreen = img[:, :, 1]
# imgRed = img[:, :, 2]

# # displaying all three images at once
# new_img = np.hstack( (imgBlue, imgGreen, imgRed) )
# cv2.imshow("My First Image", new_img)
# cv2.waitKey(0) 

# # showing image
# cv2.imshow("My First Image", img)
# cv2.waitKey(0) 


# converting image in grayscale image
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("window", img_gray)
# cv2.waitKey(0) 


# # resizing the image
# img_resize = cv2.resize(img, (800,800))
# cv2.imshow("Image Resized", img_resize)
# cv2.waitKey(0)


# # decreasing the images to half of its original size
# img_half = cv2.resize(img, (img.shape[0]//2, img.shape[1]//2) )
# cv2.imshow("Image reduced by half", img_half)
# cv2.imshow("Original Image", img)
# cv2.waitKey(0)


# # flipping the image
# # 0 means 180 degree, 1 means 360 degree
# # 0 means flip by Vertical Axis and 1 means flip by Horizontal Axis
# # -1 means flip by both vertical and horizontal axis
# img_flip = cv2.flip(img, -1)
# cv2.imshow("Image reduced by half", img_flip)
# cv2.waitKey(0)


# # cropping the image ['height axis', 'width axis']
# img_crop = img[:, 200:500]
# cv2.imshow("Cropping the image", img_crop)
# cv2.waitKey(0)

# # cropping from top ['height axis', 'width axis']
# img_crop1 = img[0:100, 0:100]
# cv2.imshow("Original Image", img)
# cv2.imshow("Cropping the image from top side", img_crop1)
# cv2.waitKey(0)


# # # saving the image
# # converting the image to only Blue, Green, Red
# img_saved1, img_saved2, img_saved3= img.copy(), img.copy(), img.copy()
# img_saved1[:,:, 0] = 0
# img_saved2[:,:, 1] = 0
# img_saved3[:,:, 2] = 0
# img_saved4 = np.hstack( (img_saved1, img_saved2, img_saved3) )
# cv2.imwrite(r".\ImageProcessing\Saved_Blue_Img88.jpg", img_saved2)
# cv2.imshow("Saving the image", img_saved4)
# cv2.waitKey(0)


# # creating your own image
# # creating an black window
# img_created = img = np.zeros( (512, 512, 3))
# # creating a rectangle in the created black window
# cv2.rectangle(img_created, pt1=(100,100), pt2=(300,300), color=(255,0,0), thickness=3)
# # creating a rectangle in the created black window with color filled in it
# cv2.rectangle(img_created, pt1=(150,150), pt2=(300,300), color=(255,0,0), thickness=-100)
# # creating a circle in the created black window
# cv2.circle(img_created, center=(225,225), radius=50, color=(0,255,255), thickness=2)
# # creating a circle in the created black window with color filled in it
# cv2.circle(img_created, center=(225,225), radius=20, color=(0,255,255), thickness=-1)
# # creating a line in the created black window
# cv2.line(img_created, pt1=(100, 100), pt2=(150, 150), color=(0,0,255), thickness=3)
# # inserting the image in the window
# cv2.putText(img_created, org=(100, 400), fontScale=1, color=(255,0,255), thickness = 2, lineType=cv2.LINE_AA, text="This is my first text", fontFace=cv2.FONT_HERSHEY_TRIPLEX)
# cv2.imshow("Created Image1", img_created)
# cv2.waitKey(0)


# Live Drawing

# -- Event Handle --
# # Inserting Circle on click
# # creating an black window
# img_created2 = img = np.zeros( (512, 512, 3))

# while True:
#     cv2.imshow("Live Drawing", img_created2)
    
#     if cv2.waitKey(1) & 0xFF == ord('x'):
#         break

# # destroy all the windows
# cv2.destroyAllWindows()


# #  --- Complex Even Handling ---
# # ye parameter daalne jaroorri hai
# # It is necessay to enter these parameters
# def draw(event,x,y,flags,params):
#     print(event,x,y,flags,params)

# cv2.namedWindow(winname="Complex_Event_Handling")
# cv2.setMouseCallback("Complex_Event_Handling", draw)

# img_created2 = img = np.zeros( (512, 512, 3))

# while True:
#     cv2.imshow("Complex_Event_Handling", img_created2)
    
#     if cv2.waitKey(1) & 0xFF == ord('x'):
#         break

# # destroy all the windows
# cv2.destroyAllWindows()



# # making the square using event handling
# drawing = False
# ix = -1
# iy = -1

# def draw(event,x,y,flags,params):    
    
#     global drawing, ix, iy
    
#     if event == 1:
#         print("Mouse-Clicked : Start Drawing")
#         drawing = True
#         ix = x
#         iy = y    

#     elif event == 0 and drawing == True:
#         print("Mouse-Draging : Start Drawing")        
#         # cv2.rectangle(img_created3, pt1=(ix,iy), pt2=(x,y), color=(0,0,255), thickness=2)

#     elif event == 4:
#         drawing = False
#         cv2.rectangle(img_created3, pt1=(ix,iy), pt2=(x,y), color=(0,0,255), thickness=2)

# cv2.namedWindow(winname="Complex_Event_Handling")
# cv2.setMouseCallback("Complex_Event_Handling", draw)

# img_created3 = img = np.zeros( (512, 512, 3))

# while True:
#     cv2.imshow("Complex_Event_Handling", img_created3)
    
#     if cv2.waitKey(1) & 0xFF == ord('x'):
#         break

# # destroy all the windows
# cv2.destroyAllWindows()


# # making the cropping tool using event handling
# drawing = False
# ix = -1
# iy = -1

# def draw(event,x,y,flags,params):    
    
#     global drawing, ix, iy
    
#     if event == 1:
#         print("Mouse-Clicked : Start Drawing")
#         drawing = True
#         ix = x
#         iy = y    

#     elif event == 0 and drawing == True:
#         print("Mouse-Draging : Start Drawing")        
#         cv2.rectangle(img_created3, pt1=(ix,iy), pt2=(x,y), color=(0,0,255), thickness=2)

#     elif event == 4:
#         drawing = False
#         # cv2.rectangle(img_created3, pt1=(ix,iy), pt2=(x,y), color=(0,0,255), thickness=2)

# cv2.namedWindow(winname="Complex_Event_Handling")
# cv2.setMouseCallback("Complex_Event_Handling", draw)

# img_created3 = img = np.zeros( (512, 512, 3))

# while True:
#     cv2.imshow("Complex_Event_Handling", img_created3)
    
#     if cv2.waitKey(1) & 0xFF == ord('x'):
#         break

# # destroy all the windows
# cv2.destroyAllWindows()



# # making the cropping tool using event handling
# drawing = False
# ix = -1
# iy = -1

# def draw(event,x,y,flags,params):    
    
#     global drawing, ix, iy
    
#     if event == 1:
#         print("Mouse-Clicked : Start Drawing")
#         drawing = True
#         ix = x
#         iy = y    

#     elif event == 0 and drawing == True:
#         print("Mouse-Draging : Start Drawing")        
#         # cv2.rectangle(img_created3, pt1=(ix,iy), pt2=(x,y), color=(0,0,255), thickness=2)

#     elif event == 4:
#         drawing = False
#         # saving the cropped image
#         img_copy = img.copy()
#         cv2.rectangle(img, pt1=(ix,iy), pt2=(x,y), color=(0,0,255), thickness=2)
        

#         # it is img[height, width]
#         save_image = img_copy[min(iy-1, y-1):max(iy-1, y-1), min(ix-1, x-1):max(ix-1, x-1)]
#         cv2.imwrite(r".\ImageProcessing\Cropped_image.jpg", save_image)
#         cv2.imshow("Saving the image", save_image)


# cv2.namedWindow(winname="Crop the window")
# cv2.setMouseCallback("Crop the window", draw)

# while True:
#     cv2.imshow("Crop the window", img)
    
#     if cv2.waitKey(1) & 0xFF == ord('x'):
#         break

# # destroy all the windows
# cv2.destroyAllWindows()


# handling videos using opencv

# capturing video by webcam 
import cv2

cap = cv2.VideoCapture(0)
# fetching the exat dimenrsions of webcam
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# saving the image
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(r"./SavedVideo4.avi", fourcc,20.00, (frame_width, frame_height))

while True:
    ret, frame = cap.read()
    
    img_edited = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    out.write(img_edited)

    cv2.imshow("webcam", frame)
    print(ret)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()


