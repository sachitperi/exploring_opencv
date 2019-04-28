"""
Goal:
* to draw different geometric shapes with opencv
* Learn functions
    --> cv2.line()
    --> cv2.circle()
    --> cv2.rectangle()
    --> cv2.ellipse()
    --> cv2.putText()

In all the above functions we will use the following common arguments
    * img : The image where you want to draw the shapes
    * color : color of the shape. For BGR pass it as tuple eg: (255, 0, 0) for blue. For grayscale pass the scalar value
    * thickness : Thickness of the line or circle etc. If -1 is passed for closed figures like circles, it will fill the shape. default thickness = 1
    * line type : Type of line, 8-connected, anti-aliased line, etc. By default it is 8-connected. cv2.Line_AA gives anti aliased line which looks great for curves
"""

import numpy as np
import cv2

# Drawing a line
# to draw a line we need to specify the starting and ending coordinates of the line

# cretae a black image
img = np.zeros((512, 512, 3), np.uint8)

#Draw a diagonal blue line with thickness of 5 px
cv2.line(img, (0,0), (512, 512), (255, 0, 0), thickness=5)

#Draw Rectangle
# To draw a rectangle we need top lef and bottom right corner coordinates.
cv2.rectangle(img, (100, 100), (400, 200), (0, 255, 0), thickness=10)

# Drawing a circle
# need centre coordinates and radius
cv2.circle(img, (150, 300), 100, (0, 0, 255), thickness=4)

# Drawing elipse
# found little useless can check the docs id needed

# Drawing a polygon
# need coordinates of vertices. make those points into array of shape rows*1*2 where rows are number of vertices and it should be of type int.
#all lines will be drawn individually. More better way to call cv2.line() individually
pts = np.array([[10, 15], [60, 30], [100, 70], [200, 80], [400, 100]], np.int32)
cv2.polylines(img, [pts], True, (0, 255, 255), thickness=4)

# Adding Text to image
"""
required: 
* text data want to write
* position coordinates where to put the text
* font type
* font scale
* regular thing  like color thickness etc
"""

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (0, 300), font, 2, (255, 0, 255), thickness=2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()