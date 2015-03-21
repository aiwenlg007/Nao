from naoqi import ALProxy  
  
memProxy = ALProxy("ALMemory","192.168.31.238",9559)  
print memProxy.getData("Device/SubDeviceList/LShoulderPitch/Position/Sensor/Value")        
print memProxy.getData("Device/SubDeviceList/InertialSensor/GyrX/Sensor/Value")  
print memProxy.getData("Device/SubDeviceList/InertialSensor/GyrY/Sensor/Value") 
#print memProxy.getData("Device/SubDeviceList/InertialSensor/GyrRef/Sensor/Value")  
