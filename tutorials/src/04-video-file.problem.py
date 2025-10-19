# Exercise #4
# -----------
#
# Loading a video file and mirror it.


#  Just copy the code from exercise 3 and modify it to load a video file instead of the camera.
# Use the file "tutorials/data/videos/hello_UH.m4v" as input for the 'VideoCapture' function.

import numpy as np
import cv2


cap = cv2.VideoCapture("tutorials/data/videos/hello_UH.m4v")



print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
title = "webcam"
cv2.namedWindow(title, cv2.WINDOW_NORMAL)


while True: 

    ret, frame = cap.read()

    if ret:
       
        key =  cv2.waitKey(20)
        img = np.zeros_like(frame)
        tile = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
        img[:tile.shape[0], :tile.shape[1]] = tile
        img[tile.shape[0]:, :tile.shape[1]] = cv2.flip(tile, 0)
        img[:tile.shape[0], tile.shape[1]:] = cv2.flip(tile, 1)
        img[tile.shape[0]:, tile.shape[1]:] = cv2.flip(tile, -1)
       
        cv2.imshow(title, img)

        
        if key == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()