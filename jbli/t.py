from naoqi import ALProxy
#ip="192.168.31.238"
tts = ALProxy("ALTextToSpeech", "192.168.31.238", 9559)
tts.say("Hello, world!")
