# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import xarm
import ikpy.chain

# arm is the first xArm detected which is connected to USB
arm = xarm.Controller('USB')
my_chain = ikpy.chain.Chain.from_urdf_file("xArm_with_gripper.urdf")

print('Battery voltage in volts:', arm.getBatteryVoltage())
arm.setPosition(6, 500)