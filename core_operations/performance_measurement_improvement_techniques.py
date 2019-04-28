"""
Goal:
Learn to measure performance of the code
Tips to improve performance of the code
cv2.getTickCount(), cv2.getTickFrequency()

Apart from opencv python also provides a module time which is helpful in measuring time of execution.
Another module Profile helps to get detailed report on the code (like howmuch time each function of the code took, howmany times the function was called etc)

"""

# Measuring performing with opencv

"""
cv2.getTickCount function returns the number of clock-cycles after a reference event (like the moment machine was switched ON) to the moment this function is called. 
So if you call it before and after the function execution, you get number of clock-cycles used to execute a function.

cv2.getTickFrequency function returns the frequency of clock-cycles, or the number of clock-cycles per second. 
So to find the time of execution in seconds, you can do following:
"""

import numpy as np
import cv2

img = cv2.imread('../images/messi5.jpg')

t1 = cv2.getTickCount()
for i in range(5,49,2):
    img = cv2.medianBlur(img,i)

e2 = cv2.getTickCount()
t2 = cv2.getTickCount()
time = (t2 - t1)/cv2.getTickFrequency()
print(t1, t2, time)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Default optimization in opencv
"""
Opencv is optimized using SSE2, AVX etc. It contains unoptimized code also.
It is enabled by default while compiling
Check if opencv is using optimized code using cv2.useOptimized()

"""
print(cv2.useOptimized())