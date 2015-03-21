import naoqi
from naoqi import ALProxy

dcm = ALProxy("DCM","192.168.31.238",9559)

memProxy = ALProxy("ALMemory","192.168.31.238",9559)
#print memProxy.getData("Device/SubDeviceList/HeadPitch/Position/Actuator/Value")
#print dcm.getTime(0)

#dcm.set(["Device/SubDeviceList/LShoulderRoll/Position/Actuator/Value", "ClearAll", [[10.0,dcm.getTime(10000)]] ])
# dcm.set(["Device/SubDeviceList/HeadPitch/Position/Actuator/Value", "ClearAll", [[0.2,dcm.getTime(2000)],[-0.1,dcm.getTime(4000)],[-0.3,dcm.getTime(6000)]]])

dcm.set(["Device/SubDeviceList/HeadPitch/Position/Actuator/Value", "ClearAll", [[-0.1,dcm.getTime(0)]]])

#dcm.set(["Device/SubDeviceList/HeadYaw/Position/Actuator/Value", "ClearAll", [[0.3,dcm.getTime(0)],[0.5,dcm.getTime(4000)]]])