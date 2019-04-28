"""
Goal:
How to convert images from one color space to another, like BGR to gray, BGR to HSV
Create an application that extracts a colored object in a video

Functions:
cv2.cvtColor()
cv2.inRange()
"""

# Changing color spaces
"""
more than 150 colorspace conversions available in opencv
look at BGR to Gray and BGR to HSV
use cv2.cvtColor(input_image, flag) where flag determines the type of conversion
for BGR to Gray use cv2.COLOR_BGR2GRAY
for BGR to HSV use cv2.COLOR_BGR2HSV

"""

import cv2

img = cv2.imread('../images/messi5.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('gray', gray)
cv2.imshow('hsv', hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Object Tracking
"""
In HSV it is more easier to represent color than RGB space
We will try to extract Blue colored objects
    * Take each frame of a video
    * Convert BGR to HSV
    * We threshold the HSV image for a range of blue color
    * Now extract the blue object alone we can do whatever we want.
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    # Take each frame
    res, frame = cap.read()

    #conbvert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #define range of blue color in HSV
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    #threshold the hsv image to get only blue color
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    #Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()

#How to find HSV values to track?

"""
This is a common question found in stackoverflow.com. It is very simple and you can use the same function, cv2.cvtColor(). Instead of passing an image, you just pass the BGR values you want. For example, to find the HSV value of Green, try following commands in Python terminal:

>>> green = np.uint8([[[0,255,0 ]]])
>>> hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
>>> print hsv_green
[[[ 60 255 255]]]
Now you take [H-10, 100,100] and [H+10, 255, 255] as lower bound and upper bound respectively. Apart from this method, you can use any image editing tools like GIMP or any online converters to find these values, but don’t forget to adjust the HSV ranges.


"""