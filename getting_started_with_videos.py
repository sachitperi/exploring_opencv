"""
Goal:
*Learn to
    -- Read Video
    --Display Video
    -- Save Video
* Learn to
    -- Capture from camera and display it
* Learn Functions
    -- cv2.VideoCapture()
    -- cv2.VideoWriter()
"""

import numpy as np
import cv2

"""
To capture a video you need to create the VideoCapture object.
Its argument can either be a device index or name of a video file.
    Device index is just the number to specify which camera. Normally only one camera is connected (so pass 0 or -1). If more than one camera is connected then pass the camera number
After that you can capture frame by frame. Also release the capture after your output is released

VideoCapture api has the following objects
VideoCapture.open() #The methods first call VideoCapture::release() to close the already opened file or camera.
VideoCapture.isOpened() #If the previous call to VideoCapture constructor or VideoCapture::open succeeded, the method returns true.
VideoCapture.release() #The methods are automatically called by subsequent VideoCapture::open() and by VideoCapture destructor. The C function also deallocates memory and clears *capture pointer.

VideoCapture.grab()
# The method grabs the next frame of the video file or camera and return true(non-zero) in case of success
primary us is in multi camera environments, especially when cameras donot have hardware synchronization
cv2.VideoCapture.grab() → retval
cv.GrabFrame(capture) → int

VideoCapture.retrieve()
The method function decodes and returns the just grabbed frame. 
If no frames has been grabbed (camera disconnected or no more frames in the video the method returns false and functions return Null pointer
cv2.VideoCapture.retrieve([image[, channel]]) → retval, image
cv.RetrieveFrame(capture[, index]) → image


VideoCapture.read()
The method/function combines VideoCapture.grab() and VideoCapture.retrieve() in one call. This is the most convineant method for reading video files 
or capturing data from decode and return the just grabbed frame.
If no frames grabbed (camera disconnected or no more frames in video), the methods return False and functions return null pointer
cv2.VideoCapture.read([image]) → retval, image
 
VideoCapture.Get()
VideoCapture.Set()

"""
cap = cv2.VideoCapture(0)
print(cap.isOpened()) #used to check if the capture is happening

#A way to use grab and retrieve function
# ret = cap.grab()
# re, frame = cap.retrieve()
# cv2.imshow('me', frame)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

while(True):
    # capture frame by frame
    ret, image = cap.read()

    # our operations on frame come here
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # display the resulting frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# when everything is done
cap.release()
cv2.destroyAllWindows()

#playing video from a file
cap = cv2.VideoCapture('/Users/sachitanandp/Dropbox (21st Century Fox)/my_material/pet_proj/embeded_marketting/overview/929823485.mp4')
# cap = cv2.VideoCapture('./tut/images/output.avi')
print(cap.isOpened())

while(True):
    ret, image = cap.read()

    # graying out the video
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # displaying the resulting frame
    cv2.imshow('gray_video', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

# import numpy as np
# import cv2
# already imported in the begining

"""
writing a video is not as simple as writing an image (cv2.imwrite()).
Initiate a video writer object
    --> specify the name of the output video file
    --> Specify the Fourcc codec
        *  Fourcc is a 4-byte code used to specify the video codec. The codec is platform dependent
            In Fedora: DIVX, XVID, MJPG, X264, WMV1, WMV2. (XVID is more preferable. MJPG results in high size video. X264 gives very small size video)
            In OSX : (I don’t have access to OSX. Can some one fill this?) 
    --> No of frames per second and 
    --> then the frame size 
"""

cap = cv2.VideoCapture(0)

# Define the codec and create video writer object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('./tut/images/output.avi', fourcc, 20.0, (640, 480))

while(cap.isOpened()):
    ret, image = cap.read()

    if ret == True:
        image = cv2.flip(image, 0)

        # write the flipped frame
        out.write(image)

        cv2.imshow('image', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
