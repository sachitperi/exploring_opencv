"""
Goals:
How to
* Read an Image
* Display the image
* Store it back

Functions to learn
cv2.imread()
cv2.imshow()
cv2.imwrite()
"""

import numpy as np
import cv2

"""
imread function take 2 arguments 
* path of the image 
* flag which specifies the way image should be read
    cv2.IMREAD_COLOR      : loads a color image
    cv2.IMREAD_GRAYSCALE  : load a grayscale image
    cv2.IMREAD_UNCHANGED  : loads image assuch include alpha channel
"""
img_color = cv2.imread('./tut/images/messi5.jpg', cv2.IMREAD_COLOR)
img_gray = cv2.imread('./tut/images/messi5.jpg', cv2.IMREAD_GRAYSCALE)
img_uc = cv2.imread('./tut/images/messi5.jpg', cv2.IMREAD_UNCHANGED)

print('color images shape', img_color.shape)
print('grayscale images shape', img_gray.shape)
print('unchanged images shape', img_uc.shape)

cv2.imshow('messi_color', img_color) # used to display an image , takes 2 arguments name to be displayed and matrix containing images detail
cv2.imshow('messi_gray', img_gray)
cv2.imshow('messi_uc', img_uc)

"""
cv2.waitKey() is a keyboard binding function. Its argument is the time in milliseconds. 
The function waits for specified milliseconds for any keyboard event. If you press any key in that time, the program continues. 
If 0 is passed, it waits indefinitely for a key stroke. It can also be set to detect specific key strokes like, if key a is pressed etc which we will discuss below.
*** Note: Besides binding keyboard events this function also processes many other GUI events, so you MUST use it to actually display the image.
"""
cv2.waitKey(0)

cv2.destroyAllWindows() # destroys all windows we created. If to destroy specific window use cv2.destroyWindow() function where you pass the window name as argument

"""
There is a special case where you can already create a windoe and load an image to it later
in that case you can specify if window is resizable or not
* done using function cv2.namedWindow() 
By default, the flag is cv2.WINDOW_AUTOSIZE, but by specifing cv2.WINDOW_NORMAL you can resize window. 
It will be helpful when image is too large in dimensions and adding trackbar to windows 
"""

cv2.namedWindow('messi_load_after', cv2.WINDOW_NORMAL)
cv2.imshow('messi_load_after', img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Writing an image
cv2.imwrite('./tut/images/messi_gray_write.jpg', img_gray)

"""

"""
# import numpy as np
# import cv2
# The imports have already been done at the begining of the script

img = cv2.imread('./tut/images/messi5.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('messi_gray', img)
k = cv2.waitKey(0)
if k == 27: # wait for any other key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for s key to save and exit
    cv2.imwrite('./tut/images/messi_gray.jpg', img)
    cv2.destroyAllWindows()

# display using matplotlib

# import numpy as np
# import cv2
# the imports were done at the begining of the script
import matplotlib.pyplot as plt

img = cv2.imread('./tut/images/messi5.jpg')
print(img.shape)
# img_rgb = img[:,:,::-1]
img_rgb = np.stack((img[:,:,2], img[:,:,1], img[:,:,0]), axis=2)
print(img_rgb.shape)
# plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([]) #to hide the tics
plt.imshow(img_rgb)
plt.show()


# Note: Color images loaded by opencv is in BGR mode. But matplotlib displays in RGB mode. So color images will not be displayed correctly in matplotlib
# if image is read with opencv.


