# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import xarm
import ikpy.chain
import math
import matplotlib.pyplot
from mpl_toolkits.mplot3d import Axes3D
import time

# arm is the first xArm detected which is connected to USB
my_chain = ikpy.chain.Chain.from_urdf_file("xArm_with_gripper.urdf")

ax = matplotlib.pyplot.figure().add_subplot(111, projection='3d')
my_chain.plot(my_chain.inverse_kinematics([2, 2, 2]), ax)
matplotlib.pyplot.show()

def sendAngles(angles):
    angles = [float(item) for item in angles]
    arm = xarm.Controller('USB')
    arm.setPosition(6, angles[1])
    time.sleep(0.01)
    arm.setPosition(2, angles[5])
    time.sleep(0.01)
    arm.setPosition(3, -angles[4])
    time.sleep(0.01)
    arm.setPosition(4, angles[3])
    time.sleep(0.01)
    arm.setPosition(5, angles[2])

def calcAngles(x,y,z):
    res = my_chain.inverse_kinematics([x,y,z])
    
    matplotlib.pyplot.clf()
    ax = matplotlib.pyplot.figure().add_subplot(111, projection='3d')
    my_chain.plot(my_chain.inverse_kinematics([x, y, z]), ax)
    matplotlib.pyplot.show()
    print(res)
    res = [math.degrees(item) for item in res]
    return res

def controlArm(x,y,z):
    angles = calcAngles(x,y,z)
    print (angles)
    sendAngles(angles)
    
def grab():
    arm = xarm.Controller('USB')
    arm.setPosition(1,1000)

def release():
    arm = xarm.Controller('USB')
    arm.setPosition(1,0)
    
def main():
    release()
    controlArm(0,0,0.1)
    time.sleep(1)
    controlArm(0.2,0,0.1)
    time.sleep(1)
    controlArm(0.2,0,0.2)
    time.sleep(1)
    controlArm(0,0.2,0.1)
    time.sleep(1)
    controlArm(0,0.1,0.1)
    time.sleep(1)
    controlArm(-0.2,0,0.1)
    time.sleep(1)
    controlArm(-0.2,0,0.2)
    time.sleep(1)
    controlArm(0,0,0.3)
    time.sleep(1)
    controlArm(0,0,0.15)
    time.sleep(1)
    grab()
    controlArm(0.15,0.15,0.1)
    time.sleep(2)
    controlArm(0.05,-0.1,0.1)
    time.sleep(1)
    
main()
    