#!/usr/bin/env python
import rospy
import time
import sys
import numpy as np
import cv2
import requests as r
from sensor_msgs.msg import Image
from camera_info_manager import *
from cv_bridge import CvBridge, CvBridgeError

rospy.init_node("ipcam_to_ros")

publeft = rospy.Publisher('left/image_raw', Image, queue_size=10)
pubright = rospy.Publisher('right/image_raw', Image, queue_size=10)

bridge=CvBridge()

rate_limit=rospy.get_param("~rate_limit",30)

left_cam_ip=rospy.get_param('~left_cam_ip', None)
right_cam_ip=rospy.get_param('~right_cam_ip', None)

left_config=rospy.get_param('~left_config',"file://home/daruis1/l.yaml")
right_config=rospy.get_param('~right_config',"file://home/daruis1/r.yaml")

def fetch_image_msg(cam_ip):
    try:
        req=r.get("http://{0}/shot.jpg".format(cam_ip))
    except:
        rospy.logerror("Can't fetch cam {0}".format(cam_ip))
        return None
    image = np.asarray(bytearray(req.content), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    try:
         img_msg = bridge.cv2_to_imgmsg(image, "bgr8")
    except CvBridgeError as e:
        rospy.logerror(e)
        return None
    return img_msg  

def leftCall():
    img=fetch_image_msg(left_cam_ip)
    if img:
        publeft.publish(img)

def rightCall():
    img=fetch_image_msg(right_cam_ip)
    if img:
        pubright.publish(img)


    

if left_cam_ip==None or right_cam_ip==None:
    rospy.logfatal("cam IP is not set")
    sys.exit(1)
if __name__=="__main__":
    rospy.loginfo("setting nofocus=True")
    
    r.get("http://{0}/nofocus".format(left_cam_ip))
    r.get("http://{0}/nofocus".format(right_cam_ip))

    rospy.loginfo("Setting Up Services...")    
    CameraInfoManager(cname="left",url=left_config,namespace="left")
    CameraInfoManager(cname="right",url=right_config,namespace="right")
    rate=rospy.Rate(rate_limit)
    while not rospy.is_shutdown():
        leftCall()
        rightCall()
        rate.sleep()