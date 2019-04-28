"""
Goal:
Learn to build trackbar to opencv windows
learn functions:
cv2.getTrackbarPos()
cv2.createTrackbar()
"""

"""
create an application 
shows the color you specify
window which shows color and 3 trackbars each for B, G, R colors

cv2.getTrackbarPos()
    Inputs: (to be provided in the same order) 
    --> trackbar name
    --> window name to which it is attached
    --> default value
    --> maximum value
    --> callback function (has a default value which is trackbar position )

Another important application of trackbar is to have a button like functionality
"""

import cv2
import numpy as np

def nothing(x):
    pass

# creata ablack image and a window
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')

# create trackbars for colorchange
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)

# create a switch with on of functionality
switch = '0 : OFF\n1 : ON'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)

while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    s = cv2.getTrackbarPos(switch, 'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv2.destroyAllWindows()