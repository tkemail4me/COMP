import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
import time

GPIO.setup(21,GPIO.IN)
GPIO.setup(26,GPIO.OUT)
input = GPIO.input(21)
a=0

while True:
    if (GPIO.input(21)):
        print('Button has been Pressed', a+1, 'times')
        a=a+1
        time.sleep(0.2)
        count = 0
        while count < 3:
            GPIO.output(26, 1)
            time.sleep(0.2)
            GPIO.output(26, 0)
            time.sleep(0.2)
            count=count+1
            
        