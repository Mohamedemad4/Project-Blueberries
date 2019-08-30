#!/usr/bin/env python
import rospy
import time
import cv2
import random
import numpy as np
from sensor_msgs.msg import Image,PointCloud2
from cv_bridge import CvBridge, CvBridgeError
"""
rot90 -90 degress clockwise
rot90 axes=(1,0) +90 clockwise
"""
size=(24,15)
a=[]
bridge=CvBridge()
def leftCall(data):
    try:
         cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
        rospy.logerror(e)
        return
    if cv2.findChessboardCorners(cv_image,size)[0]==True:
        x=random.randint(1,4000)
        print(cv2.imwrite("sim1/left/{0}.png".format(x),cv_image))
        print("SAVING: left",x)
def rightCall(data):
    try:
         cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
        rospy.logerror(e)
        return
    if cv2.findChessboardCorners(cv_image,size)[0] ==True:
        x=random.randint(1,4000)
        print(cv2.imwrite("sim1/right/{0}.png".format(x),cv_image))
        print("SAVING: right",x)
rospy.init_node("rotate_images")
    
def pp(data):
    print(data.header.frame_id)
#rospy.Subscriber("left/image_raw", Image, leftCall)
#rospy.Subscriber("right/image_raw", Image, rightCall)
rospy.Subscriber("/points2",PointCloud2,pp)
if __name__=="__main__":
    rospy.loginfo("Starting stero _save sub")
    rospy.spin()
    