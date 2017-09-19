#!/usr/bin/env python
# Scripts for iros challenge 5: unplug main and usb light
#                               re-plug main and usb light
import time
import copy
import math

import cv2
import imutils
from matplotlib import pyplot as plt

import iros_interface_cmds as ic
import iros_waypoints as iw
#import vision_copy as vc

def begin(c,ser_ee):

    # Location of USB top middle

    x_u = 100
    y_u = 200
    height_u = 40

    # Location of light
    x_l = 100
    y_l = 150
    height_l = 50

    demand_Grip = dict(ee_home)
    msg = ic.safe_move(c,ser_ee,Pose=dict(iw.grab_joints),Grip=demand_Grip,CMD=2)

    # Goto position of USB light
    demand_Pose = dict(home)
    demand_Pose["x"] = x_u
    demand_Pose["y"] = y_u
    msg = ic.safe_ur_move(c,Pose=demand_Pose,CMD=4)

    # Lower to USB
    demand_Pose["z"] = height_u
    msg = ic.safe_ur_move(c,Pose=demand_Pose,CMD=4)

    # Close Gripper
    demand_Grip["servo"]=10
    msg = ic.end_effector_move(ser_ee,demand_Grip)

    #Pull out
    demand_Pose["z"] = height_u + 40
    msg = ic.safe_ur_move(c,Pose=demand_Pose,CMD=4)

    #Push in
    demand_Pose["z"] = height_u - 5
    msg = ic.safe_ur_move(c,Pose=demand_Pose,CMD=4)

    # Release Gripper
    demand_Grip["servo"]=80
    msg = ic.end_effector_move(ser_ee,demand_Grip)


    # Goto position of light
    demand_Pose["x"] = x_l
    demand_Pose["y"] = y_l
    msg = ic.safe_ur_move(c,Pose=demand_Pose,CMD=4)

    # Lower to light
    demand_Pose["z"] = height_l
    msg = ic.safe_ur_move(c,Pose=demand_Pose,CMD=4)

    # Close Gripper
    demand_Grip["servo"]=10
    msg = ic.end_effector_move(ser_ee,demand_Grip)

    # Pull out
    demand_Pose["z"] = height_u + 40
    msg = ic.safe_ur_move(c,Pose=demand_Pose,CMD=4)

    # Push in  
    demand_Pose["z"] = height_u - 5
    msg = ic.safe_ur_move(c,Pose=demand_Pose,CMD=4)

    # Release Gripper
    demand_Grip["servo"]=80
    msg = ic.end_effector_move(ser_ee,demand_Grip)
