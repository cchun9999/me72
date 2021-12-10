#!/usr/bin/env python
#
# Used for initial testing of the camera
# by writing camera image to a jpg

import cv2

cam = cv2.VideoCapture(0)

while True:
    ret, image = cam.read()
    cv2.imshow('Imagetest',image)
    k = cv2.waitKey(1)
    if k != -1:
        break
cv2.imwrite('/home/pi/Desktop/testimage.jpg', image)
cam.release()
cv2.destroyAllWindows()