import time
import math

from naoqi import ALProxy

IP = "192.168.31.238"  # Replace here with your NaoQi's IP address.
PORT = 9559

# Create a proxy to ALLandMarkDetection
try:
  landMarkProxy = ALProxy("ALLandMarkDetection", IP, PORT)
except Exception, e:
  print "Error when creating landmark detection proxy:"
  print str(e)
  exit(1)

# Subscribe to the ALLandMarkDetection proxy
# This means that the module will write in ALMemory with
# the given period below
period = 500
landMarkProxy.subscribe("Test_LandMark", period, 0.0 )

# ALMemory variable where the ALLandMarkdetection modules
# outputs its results
memValue = "LandmarkDetected"

# Create a proxy to ALMemory
try:
  memoryProxy = ALProxy("ALMemory", IP, PORT)
except Exception, e:
  print "Error when creating memory proxy:"
  print str(e)
  exit(1)
#¼ÆËã×ø±ê
def CalcPos( theltaX ,alf,bta ):  
	mkRadius = (3.52/2)/100
	mkDistance = mkRadius/math.tan(theltaX/2) 
	dOT = mkDistance*math.cos(bta)
	deltaX = dOT*math.cos(alf)*100
	deltaY = dOT*math.sin(alf)*100
	deltaZ = dOT*math.sin(bta)*100
	distance = mkDistance * 100
	print "distance = %0.3f,deltaX = %0.3f,deltaY = %0.3f,deltaZ = %0.3f" % (distance,deltaX,deltaY,deltaZ)
	return 0
   

# A simple loop that reads the memValue and checks whether landmarks are detected.
for i in range(0, 20):
  time.sleep(0.5)
  val = memoryProxy.getData(memValue)

  print ""
  print "*****"
  print ""

  # Check whether we got a valid output.
  if(val and isinstance(val, list) and len(val) >= 2):

    # We detected naomarks !
    # For each mark, we can read its shape info and ID.

    # First Field = TimeStamp.
    timeStamp = val[0]

    # Second Field = array of Mark_Info's.
    markInfoArray = val[1]

    try:
      # Browse the markInfoArray to get info on each detected mark.
      for markInfo in markInfoArray:

        # First Field = Shape info.
        markShapeInfo = markInfo[0]

        # Second Field = Extra info (ie, mark ID).
        markExtraInfo = markInfo[1]
        print "mark  ID: %d" % (markExtraInfo[0])
        print "  alpha %.3f - beta %.3f" % (markShapeInfo[1]*180, markShapeInfo[2]*180)
        print "  width %.3f - height %.3f" % (markShapeInfo[3]*180, markShapeInfo[4]*180)
	mkRadius = (3.52/2)/100
	mkDistance = mkRadius/math.tan(markShapeInfo[3]/2)
#	print "NaoMark distance = %.3f " % mkDistance
	
	alf = markShapeInfo[1]
	bta = markShapeInfo[2] 
	theltaX = markShapeInfo[3]
	
	CalcPos(theltaX,alf,bta)
	
    except Exception, e:
      print "Naomarks detected, but it seems getData is invalid. ALValue ="
      print val
      print "Error msg %s" % (str(e))
  else:
      print "No landmark detected"


# Unsubscribe the module.
landMarkProxy.unsubscribe("Test_LandMark")

print "Test terminated successfully."

