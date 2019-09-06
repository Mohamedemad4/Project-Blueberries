#!/usr/bin/env python
import rospy
import time
import sys
import numpy as np
import cv2
from threading import Thread
import requests as r
from sensor_msgs.msg import Image,CameraInfo
from camera_info_manager import *
from cv_bridge import CvBridge, CvBridgeError

rospy.init_node("ipcam_to_ros")

publeft = rospy.Publisher('left/image_raw', Image, queue_size=1)
pubright = rospy.Publisher('right/image_raw', Image, queue_size=1)

publeft_cinfo = rospy.Publisher('left/camera_info', CameraInfo, queue_size=10)
pubright_cinfo = rospy.Publisher('right/camera_info', CameraInfo, queue_size=10)

bridge=CvBridge()

rate_limit=rospy.get_param("~rate_limit",30)

left_cam_ip=rospy.get_param('~left_cam_ip', None)
right_cam_ip=rospy.get_param('~right_cam_ip', None)

left_config=rospy.get_param('~left_config',"file://home/daruis1/l.yaml")
right_config=rospy.get_param('~right_config',"file://home/daruis1/r.yaml")

rate=rospy.Rate(rate_limit)

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
    img_msg.header.stamp=rospy.Time.now()
    return img_msg  

def leftCall():
    while not rospy.is_shutdown():
        img=fetch_image_msg(left_cam_ip)
        if img:
            publeft.publish(img)
            publeft_cinfo.publish(l_cam_info.getCameraInfo())
        rate.sleep()

def rightCall():
    while not rospy.is_shutdown():
        img=fetch_image_msg(right_cam_ip)
        if img:
            pubright.publish(img)
            pubright_cinfo.publish(r_cam_info.getCameraInfo())
    rate.sleep()

    

if left_cam_ip==None or right_cam_ip==None:
    rospy.logfatal("cam IP is not set")
    sys.exit(1)
if __name__=="__main__":
    rospy.loginfo("setting nofocus=True")
    
    r.get("http://{0}/nofocus".format(left_cam_ip))
    r.get("http://{0}/nofocus".format(right_cam_ip))

    rospy.loginfo("Setting Up Services...")    
    l_cam_info=CameraInfoManager(cname="left",url=left_config,namespace="left")
    r_cam_info=CameraInfoManager(cname="right",url=right_config,namespace="right")
    
    l_cam_info.loadCameraInfo()
    r_cam_info.loadCameraInfo()
    
    rospy.loginfo("Spawing Publisher threads..")
    lc_thread=Thread(target=leftCall)
    rc_thread=Thread(target=rightCall)
    
    lc_thread.start()
    rc_thread.start()

    lc_thread.join()
    rc_thread.join()