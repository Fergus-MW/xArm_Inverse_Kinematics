# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import xarm
import ikpy.chain

# arm is the first xArm detected which is connected to USB
my_chain = ikpy.chain.Chain.from_urdf_file("xArm_with_gripper.urdf")

import matplotlib.pyplot
from mpl_toolkits.mplot3d import Axes3D
ax = matplotlib.pyplot.figure().add_subplot(111, projection='3d')

my_chain.plot(my_chain.inverse_kinematics([2, 2, 2]), ax)
matplotlib.pyplot.show()
def sendAngles(angles):
    arm = xarm.Controller('USB')
    print('Battery voltage in volts:', arm.getBatteryVoltage())
    arm.setPosition(1, angles[0])
    arm.setPosition(2, angles[1])
    arm.setPosition(3, angles[2])
    arm.setPosition(4, angles[3])
    arm.setPosition(5, angles[4])
    arm.setPosition(6, angles[5])

def calcAngles(x,y,z):
    res = my_chain.inverse_kinematics([x,y,z])
    return res

print(calcAngles(0.1,0.1,0.1))