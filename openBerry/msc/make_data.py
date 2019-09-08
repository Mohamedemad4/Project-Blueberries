#!/usr/bin/env python
import sys
import random
import rospy
import numpy as np
from sensor_msgs.msg import PointCloud2

i=0
a=np.zeros((20,1228800))
def c(data):
    global i
    try:
        a[i]=np.fromstring(data.data)
    except:
        pass
    i+=1
    print(i)
    if i==19:
        print("DONE!")
        np.savez_compressed(open("point_cloud.npz","wb+"),data=a)
        sys.exit(0)
    return
rospy.init_node("ss")
rospy.Subscriber("/camera/depth_registered/points",PointCloud2,c)  
rospy.spin()
