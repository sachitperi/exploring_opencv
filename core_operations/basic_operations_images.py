"""
Goal:
Learn to access pixel values and modify them
Access Image properties
Setting Region of Image (ROI)
Spliting and merging images

All the operations will involve heavy use of numpy. Familiarity with numpy is a must
"""

import cv2
import numpy as np

img = cv2.imread('../images/messi5.jpg')
print('messi image shape', img.shape)

#Accessing and modifying pixels
# can access a pixel by its row and column coordinates. For BGR it returns an array of Blue, Green, Red values. For grayscale its corresponding values
px = img[100, 100]
print("pixel value is", px)

px_blue = img[100, 100, 0]
print('blue pixel value is', px_blue)
#Above mentioned method is normally used for selecting a region of array, say first 5 rows and last 3 columns like that. For individual pixel access, Numpy array methods, array.item() and array.itemset() is considered to be more better. But it always returns a scalar. So if you want to access all B,G,R values, you need to call array.item() separately for all.

# accessing red pixel value
print('red pixel value at 10, 10 is', img.item(10, 10, 2))

# modifying red pixel value
img.itemset((10, 10, 2), 100)
print('red pixel value at 10, 10 is', img.item(10, 10, 2))

# Accessing image properties
#shape of image
print('image shape', img.shape)
#total number of pixels in image
print('total images in pixel', img.size)
#datatype of the image
print('datatype of image', img.dtype)


# Image ROI
# sometime you will have to plat with certain region of image
# For eye detection in an image, first face detection is done. When face is obtained we select the face region alone and search for eyes inside it instead of searching whole image
# improves accuracy (as eyes are always on faces) and performance (as we search within a small area)

# here we are selecting the ball and copying it to another area
ball = img[200:260, 330:390]
print(ball.shape)
print(img[1:61, 1:61].shape)
img[1:61, 1:61] = ball

#Spliting and merging channels
#sometimes need top work separately on bgr channels. then split the B,G,R images to single planes.
# Other times need to join the individual channels to greate B,G,R images.

b, g, r = cv2.split(img)
img = cv2.merge((r, g, b))
"""
can also be done using b = img[:,:,0]

** cv2.split is a costly operation so do it only if necessary. On other case go for numpy indexing
"""

# ***
#Making Borders for images (Padding
"""
#If you want to create border around the image, something like a photoframe, you can use cv2.copyMakeBorder() function
the function has more applications for convolution operations, zero padding etc

cv2.copyMakeBorder()
    Inputs
    --> src                                          : Input image
    --> top, bottom, left, right                     : border width in number of pixels in corresponding directions
    --> border type                                  : Flag of what kind of boredr to be added. It can be of following types
        cv2.BORDER_CONSTANT                          : Adds a constant color border. The values should be given as next argument
        cv2.BORDER_REFLECT                           : Border will be mirror reflection of the border elements like this - fedcba|abcdefgh|hgfedcb
        cv2.BORDER_REFLECT_101 or cv2.BORDER_DEFAULT : same as above but with a slight change, like this - gfedcb|abcdefgh|gfedcba
        cv2.BORDER_WRAP                              : it will look like this - cdefgh|abcdefgh|abcdefg 
    --> value                                        : color of border if border type is cv2.BORDER_CONSTANT
 
"""

#sample code demonstrating all the border types
import cv2
import numpy as np
import matplotlib.pyplot as plt

BLUE = [255, 0, 0]

img = cv2.imread('../images/opencv_logo.png')
replicate= cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT_101)
warp = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=BLUE)

plt.subplot(231), plt.imshow(img), plt.title('original')
plt.subplot(232), plt.imshow(replicate), plt.title('replicate')
plt.subplot(233), plt.imshow(reflect), plt.title('reflect')
plt.subplot(234), plt.imshow(reflect101), plt.title('reflect101')
plt.subplot(235), plt.imshow(warp), plt.title('warp')
plt.subplot(236), plt.imshow(constant), plt.title('constant')

plt.show()

cv2.imshow('messi', img)
cv2.waitKey(0)
cv2.destroyAllWindows()