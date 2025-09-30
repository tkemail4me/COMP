import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
import time

GPIO.setup(21,GPIO.IN)
input = GPIO.input(21)

while True:
    if (GPIO.input(21)):
        print('Button is Pressed')
        time.sleep(0.2)
            
        