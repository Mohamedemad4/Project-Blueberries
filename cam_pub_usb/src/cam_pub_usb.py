#!/usr/bin/env python
import rospy
import time
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
"""
rot90 -90 degress clockwise
rot90 axes=(1,0) +90 clockwise
"""

bridge=CvBridge()
def leftCall(data):
    try:
         cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
        rospy.logerror(e)
        return
    image_new=np.rot90(cv_image,axes=(1,0))
    publeft.publish(bridge.cv2_to_imgmsg(image_new, "bgr8"))
    try:
         img_msg = bridge.cv2_to_imgmsg(image_new, "bgr8")
    except CvBridgeError as e:
        rospy.logerror(e)
        return
    publeft.publish(img_msg)

def rightCall(data):
    try:
         cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
        rospy.logerror(e)
        return
    image_new=np.rot90(cv_image,axes=(0,1))
    try:
         img_msg = bridge.cv2_to_imgmsg(image_new, "bgr8")
    except CvBridgeError as e:
        rospy.logerror(e)
        return
    pubright.publish(img_msg)

rospy.init_node("rotate_images")
    
publeft = rospy.Publisher('left/image_raw', Image, queue_size=10)
pubright = rospy.Publisher('right/image_raw', Image, queue_size=10)

rospy.Subscriber("left/image_raw_unrot", Image, leftCall)
rospy.Subscriber("right/image_raw_unrot", Image, rightCall)
if __name__=="__main__":
    rospy.loginfo("Starting Rotate_image sub")
    rospy.spin()
    