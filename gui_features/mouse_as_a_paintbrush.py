"""
Goal:
Learn to handel mouse events in opencv
Learn functions:
cv2.setMouseCallback()
"""

# Simple demo
"""
draw a circle on image whereever we click it
create a mouse callback function which is executed when a mouse event takes place
Mouse event can be anything like left button down, left button up, left button double click etc.
Gives x, y coordinates for every mouse event
with this event location we can do whatever we like 

>>> import cv2
>>> events = [i for i in dir(cv2) if 'EVENT' in i]
>>> print(events)
['EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY', 'EVENT_FLAG_LBUTTON', 'EVENT_FLAG_MBUTTON', 'EVENT_FLAG_RBUTTON', 'EVENT_FLAG_SHIFTKEY', 'EVENT_LBUTTONDBLCLK', 'EVENT_LBUTTONDOWN', 'EVENT_LBUTTONUP', 'EVENT_MBUTTONDBLCLK', 'EVENT_MBUTTONDOWN', 'EVENT_MBUTTONUP', 'EVENT_MOUSEHWHEEL', 'EVENT_MOUSEMOVE', 'EVENT_MOUSEWHEEL', 'EVENT_RBUTTONDBLCLK', 'EVENT_RBUTTONDOWN', 'EVENT_RBUTTONUP']

"""

import cv2
import numpy as np

# mouse callback function
def draw_circle(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (255, 0, 0), thickness=4)

#create a black image a window and bind the function to the window
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while(1):
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()

# More advanced demo
drawing = False
mode = True
ix, iy = -1, -1

def draw_circle(event, x, y, flags, params):
    global ix, iy, drawing, mode

    if event == cv2.EVENT_LBUTTONDBLCLK:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 0), thickness=4)
            else:
                cv2.circle(img, (ix, iy), 5, (0, 0, 255), thickness=3)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), thickness=4)
        else:
            cv2.circle(img, (ix, iy), 5, (0, 255, 0) ,thickness=5)

# bind this mouse callback function to opencv window
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(0) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()