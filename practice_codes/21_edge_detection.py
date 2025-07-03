# Edge Detection Using Canny Edge Detection Algorithm

import cv2
import numpy as np

def edge_Detection( captured_frame ):

    while 1 :
        # read the frame from the camera
        ret, frame = captured_frame.read()

        # hue - ( 0 - 179 ) in opencv
        # saturation - ( 0 - 255 ) : how much the value is mixed with white colour
        # value - ( 0 - 255 ) : how much the value is mixed with black colour

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # converting the BGR to HSV
        gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # converting the BGR to Grey

        # displaying the gray frames converted in gray_scale
        cv2.imshow("Grey", gray_scale)

        # define the range of the HSV
        lower_blue = np.array([110, 50, 50])
        upper_blue = np.array([255, 255, 180])

        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        # applying the bitwise operator - AND
        # pixels that form in this range will be represeted by 1 while the rest will be represented by 0
        result = cv2.bitwise_and(frame, frame, mask=mask)
        # showing the binary image
        cv2.imshow("bitwise frame", result)

        # showing the original image too for comaprison 
        cv2.imshow("Original Image", frame)

        # finding the strong edges by cranny algorithm
        strong_edges = cv2.Canny(frame, 100, 200)

        # display the cranny algorithm output
        cv2.imshow("Detected Strong Edges", strong_edges)

        # esc key termination window
        k = cv2.waitKey(1) & 0xff
        if k == 27:
            break
        # close the window()
    captured_frame.release()
    cv2.waitKey(1)
    cv2.destroyAllWindows()

def initiate_web_cam():
    capture_frame = cv2.VideoCapture(0)

    # passing the captured input by webcam to edge_detection function
    edge_Detection( capture_frame )
    cv2.waitKey(1)
    cv2.destroyAllWindows()

if __name__ == '__main__' :
    initiate_web_cam()