"""
Goal:
Learn several arithematic operations on images like addition, substraction, bitwise operations etc
Functions:
cv2.add()
cv2.addWeighted()
"""

"""
can add 2 images in opencv using cv2.add() or use numpy operations like res = img1 + img2
Both images should be of same depth and type or second image can just be a scalar value

There is a difference between opencv and numpy additions. In opencv addition is saturated while in numpy the addition is modulo operation.
"""

import cv2
import numpy as np

x = np.uint8([250])
y = np.uint8([10])

#image addition
print(cv2.add(x, y)) # 250 + 10 = 260 => 255

print(x + y) # 250 + 10 = 260 % 256 = 4

#more visible when you add 2 images

#image blending
# This is also image addition but different weights are given to images so that it gives a feeling of blended transperancy
# g(x) = (1-alpha)*f0(x) + alpha*f1(x) --> by varying alpha from 0 to 1 we can make a transition from one image to another

img1 = cv2.imread('../images/messi5.jpg')
img2 = cv2.imread('../images/opencv_logo.png')

# print(img1)
print(img1.shape)
print(img2.shape)

img1 = img1[:, :236, :]
img2 = img2[:280, :, :]

print(img1.shape)
print(img2.shape)

dst = cv2.addWeighted(img1, 0.4, img2, 0.6, 0)

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()


img1 = cv2.imread('../images/messi5.jpg')
img2 = cv2.imread('../images/opencv_logo.png')
# I want to put logo on top left corner so will create an ROI
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

#now create a mask of the logo and create its inverse mask also
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

#now blackout the area of logo in roi
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

#take only region of logo from logo image
img2_fg = cv2.bitwise_and(roi, roi, mask=mask)

#put logo in ROI and modify the main image
dst = cv2.add(img1_bg, img2_fg)
img1_a = img1
img1_a[0:rows, 0:cols] = dst

cv2.imshow('res', img1_a)
cv2.imshow(img1_bg)
cv2.imshow(img1_fg)
cv2.waitKey(0)
cv2.destroyAllWindows()