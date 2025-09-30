import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(21,GPIO.IN)
input = GPIO.input(21)

while True:
    if (GPIO.input(21)):
        print('Button is Pressed')

            
        