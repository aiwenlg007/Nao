import time
import math

from naoqi import ALProxy

IP = "192.168.31.238"  # Replace here with your NaoQi's IP address.
PORT = 9559
motionProxy  = ALProxy("ALMotion", IP, PORT)
postureProxy = ALProxy("ALRobotPosture", IP, PORT)

# Wake up robot
motionProxy.wakeUp()

# Send robot to Stand
postureProxy.goToPosture("StandInit", 0.5)


#####################
    ## Enable arms control by Motion algorithm
    #####################
motionProxy.setMoveArmsEnabled(True, True)
    # motionProxy.setMoveArmsEnabled(False, False)

    #####################
    ## FOOT CONTACT PROTECTION
    #####################
    #motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", False]])
motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])

    #TARGET VELOCITY
X = 0.05  #
Y = 0.0
Theta = math.pi/180*45
Frequency =0.0 # low speed
try:
    motionProxy.moveTo(X, Y, Theta)
except Exception, errorMsg:
    print str(errorMsg)
    print "This example is not allowed on this robot."
    exit()


print "moveTo terminated successfully."

