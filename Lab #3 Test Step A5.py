import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings (False)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.output(17,1)
GPIO.output(27,1)
GPIO.output(22,1)
'''GPIO.output(17,0)
GPIO.output(27,0)
GPIO.output(22,0)
'''