#!/usr/bin/env python
# End effector example:
# Send cmd code (G for grabber servo, A for DC motor actuator, V for vacuum pump)
# Then value:
# G: open 0-120 closed
# A: open 0-90 closed
# V: grab g/r release
import serial
import socket
import time
import random
import copy
import math

import cv2
import imutils
from matplotlib import pyplot as plt

import iros_interface_cmds as ic
import iros_waypoints as iw
import iros_1 as i1
import iros_2 as i2
import iros_3 as i3
import iros_4 as i4
import iros_5 as i5
import iros_6 as i6
import iros_7 as i7
import iros_8 as i8
import iros_9 as i9
import iros_10 as i10
#import vision_copy as vc

def initialize():
    #HOST = "169.254.103.235" # The remote host
    HOST = "192.168.1.105" # The remote host
    PORT = 30000 # The same port as used by the server

    print ".......................Starting Program......................."
    print ""

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT)) # Bind to the port
    s.listen(5) # Now wait for client connection.
    c, addr = s.accept() # Establish connection with client.

    print "Connected to UR"
    print ""
   
    ser_ee = serial.Serial('COM5',9600)  # open serial port
    while ser_ee.is_open==False:
        print "Waiting for serial"
    print ser_ee.name, ": ",ser_ee.readline()         # check which port was really used
    print "Ready"
    return c, ser_ee

def main():
    c, ser_ee = initialize()
    # loop
    print c.recv(1024)
    inp = raw_input("Continue?")
    msg = ic.safe_move(c,ser_ee,Pose=dict(iw.home_joints),CMD=2)
    while True:
        task = raw_input("task: ")
        if task == "s":
            while True:
                servo = int(raw_input())
                ic.serial_send(ser_ee,"T",servo)
                print "servo pos: ", servo
        if task == "1":
            print "Begin challenge 1..."
            i1.begin(c,ser_ee)
        if task == "2":
            print "Begin challenge 2..."
            i2.begin(c,ser_ee)
        if task == "3":
            print "Begin challenge 3..."
            i3.begin(c,ser_ee)
        if task == "4":
            print "Begin challenge 4..."
            i4.begin(c,ser_ee)
        if task == "5":
            print "Begin challenge 5..."
            i5.begin(c,ser_ee)
        if task == "6":
            print "Begin challenge 6..."
            i6.begin(c,ser_ee)
        if task == "7":
            print "Begin challenge 7..."
            i7.begin(c,ser_ee)
        if task == "8":
            print "Begin challenge 8..."
            i8.begin(c,ser_ee)
        if task == "9":
            print "Begin challenge 9..."
            i9.begin(c,ser_ee)
        if task == "10":
            print "Begin challenge 10..."
            i10.begin(c,ser_ee)

        if task == "pose":
            current_Pose, current_Grip = ic.get_position(c,ser_ee,CMD=1)
            print "current pose: ", current_Pose
            print "current grip: ", current_Grip
        if task == "joints":
            current_Joints, current_Grip = ic.get_position(c,ser_ee,CMD=3)
            print "current joints: ", current_Joints
            print "current grip: ", current_Grip
        if task == "grab":
            demand_Grip = dict(iw.ee_home)
            demand_Grip["act"] = int(raw_input("act: "))
            demand_Grip["servo"] = int(raw_input("servo: "))
            demand_Grip["tilt"] = int(raw_input("tilt: "))
            msg = ic.safe_move(c,ser_ee,Grip=demand_Grip, CMD=0)

if __name__ == '__main__': main()