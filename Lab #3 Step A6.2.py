#COMP2116 Lab 3 Traffic Lights
GPIO_RED=17
GPIO_AMBER=27
GPIO_GREEN=22
TIME_AMBER=1
TIME_RED=2
TIME_GREEN=2
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(GPIO_RED, GPIO.OUT)
GPIO.setup(GPIO_AMBER, GPIO.OUT)
GPIO.setup(GPIO_GREEN, GPIO.OUT)
while 1:
    #change to green
    GPIO.output(GPIO_RED, False)
    GPIO.output(GPIO_AMBER, False)
    GPIO.output(GPIO_GREEN, True)
    time.sleep(TIME_GREEN)
    #change to amber
    GPIO.output(GPIO_RED, False)
    GPIO.output(GPIO_AMBER, True)
    GPIO.output(GPIO_GREEN, False)
    time.sleep(TIME_AMBER)
    #change to red
    GPIO.output(GPIO_RED, True)
    GPIO.output(GPIO_AMBER, False)
    GPIO.output(GPIO_GREEN, False)
    time.sleep(TIME_RED)