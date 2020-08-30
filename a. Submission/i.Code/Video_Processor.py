#Video Segmentation using Canny Edge Detector
'''
Created on Wed Dec  4 11:16:03 2019
@author: IRTIQA MALIK

How to use:
    set path variable
    set prameters from trackbars
    press any key to start video edge detection 
    ouput is generated in  a folder

please use q key to exit
'''

import numpy as np 
import cv2
import os

low_threshold=0
high_threshold=0
max_threshold=1000
counter=0

#Canny edge Function
def cannyedge(img_grey):
    low_threshold=cv2.getTrackbarPos("Min Threshold","Edge_View")
    high_threshold=cv2.getTrackbarPos("Maximum Threshold","Edge_View")
    detected_edges=cv2.blur(img_grey,(3,3))
    cv2.Canny(img_grey,low_threshold,high_threshold,detected_edges,3,True)
    return detected_edges

#Named window and trackbars created 

cv2.namedWindow("Edge_View",cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar("Min Threshold","Edge_View",0,max_threshold,cannyedge)
cv2.createTrackbar("Maximum Threshold","Edge_View",0,max_threshold,cannyedge)

#Specifying the path of input video 

path='video.mp4'

#Specifying the path of output video frame folder

out_folder=path.split(".")
out_folder=str(out_folder[0])
os.system("mkdir "+out_folder)
cap = cv2.VideoCapture(path)

#Opening Video frame by frame and calling canny edge function on it

while(cap.isOpened()):
    ret, frame = cap.read() 
    if ret==True:
        
        img_grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        frame = cannyedge(img_grey)

        frame = cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)

        cv2.imshow('Edge_View',frame)
        if(counter==0):
            cv2.waitKey(0)
        out_path_is = out_folder+"/"+str(counter)+".jpg"
        counter+=1
        cv2.imwrite(out_path_is,frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break 
    else:
         break
     
#releasing video capture object

cap.release() 

#destroy all frames

cv2.destroyAllWindows()
