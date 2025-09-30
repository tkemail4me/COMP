'''
Name: Tom Kalhous
ID: 100368990
File Name: Lab3PB5.py
Description: This program senses the push button and after six presses,
the light flashes 3 times and a msg is diplayed on the screen.
'''

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
import time

GPIO.setup(21,GPIO.IN)
GPIO.setup(26,GPIO.OUT)
input = GPIO.input(21)
a=1

while True:
    if (GPIO.input(21)):
        print('Button has been Pressed', a, 'times')
        time.sleep(0.2)
        if a == 6:
            print('Half-Dozen Completed, Change Box')
            count = 0
            while count < 3:
                GPIO.output(26, 1)
                time.sleep(0.2)
                GPIO.output(26, 0)
                time.sleep(0.2)
                count=count+1
                a=0
        a=a+1
        
            
        