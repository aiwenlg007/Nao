from naoqi import ALProxy  
  
try: 
  memProxy = ALProxy("ALMemory","192.168.31.238",9559) 

  memProxy.insertData("myValueName1", "myValue1")

  #getData
  print "The value of myValueName1 is", memProxy.getData("myValueName1")

except RuntimeError,e:
  # catch exception
  print "error insert data", e 