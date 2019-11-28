#!/usr/bin/env python
import sys
import random
import rospy
import cv2
import numpy as np
from stereo_msgs.msg import DisparityImage
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
bridge=CvBridge()
i=0
i1=0
def c(data):
    global i
    i+=1
    if i % 15==0:
        cv_image = bridge.imgmsg_to_cv2(data.image, "32FC1")
        cv2.imwrite('disp_{0}.png'.format(i),cv_image)
        print("Image",i)
    return
def c2(data):
    global i1
    i1+=1
    if i1 % 30==0:
        cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
        cv2.imwrite('raw_{0}.png'.format(i1),cv_image)
        print("Image",i)
    return
rospy.init_node("ss")
rospy.Subscriber("/disparity",DisparityImage,c)  
rospy.Subscriber("/right/image_raw",Image,c2)  
print("started")
rospy.spin()
