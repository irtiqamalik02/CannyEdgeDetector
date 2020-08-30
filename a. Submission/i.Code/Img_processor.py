#Image Segementation using Canny Edge Detector

"""
Created on Sun Dec  1 23:06:01 2019

@author: Irtiqa Malik

How to use:
    set path variable
    set parameters from trackbars
    press any key to start image edge detection 
    ouput is generated in  output folder

"""
low_threshold = 0
high_threshold=0
max_threshold=1000
ratio = 3

import cv2
import os

#Specifying the path of input image 
path="../ii.Input/input.png"
#change the filename to a valid file , I've set it to input.png(no such image exists in folder) to avoid accidental change of submitted output images.

#Specifying the path of output folder 
path2="../iii.Output/output.png"
output_path=path2

def cannyedge(a):
    low_threshold=cv2.getTrackbarPos("Min Threshold","Edge_View")
    high_threshold=cv2.getTrackbarPos("Maximum Threshold","Edge_View")
    detected_edges=cv2.blur(img_grey,(27,27))
    cv2.Canny(img_grey,low_threshold,high_threshold,detected_edges,3,True)
    cv2.imshow("Edge_View",detected_edges)
    cv2.imwrite(output_path,detected_edges)

#Read Image
img_original = cv2.imread(path)

#create Mat types
img_grey = img_original.copy()
img_grey.fill(0)
dst = img_grey.copy()
detected_edges = dst.copy()

#grey conversion
img_grey=cv2.cvtColor(img_original,cv2.COLOR_BGR2GRAY)

#Canny Edge Detector called here if slider changes
cv2.namedWindow("Edge_View",cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar("Min Threshold","Edge_View",0,max_threshold,cannyedge)
cv2.createTrackbar("Maximum Threshold","Edge_View",0,max_threshold,cannyedge)
cannyedge(0)

cv2.waitKey(0)


