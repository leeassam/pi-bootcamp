#!/usr/bin/python

import sys
import RPi.GPIO as GPIO ## Import GPIO library
import time ## Time library functions
GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(7, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
speed = 1
#getting the input parms
argsLen = len(sys.argv)
if argsLen == 2:
  #Get number of times to blink LED
  blinkCount = int(sys.argv[1])
  #Blink LED the number of times specified
  for i in range(0,blinkCount):
    GPIO.output(7,True)## Switch on pin 7
    time.sleep(speed)## Wait
    GPIO.output(7,False)## Switch off pin 7
    time.sleep(speed)## Wait
GPIO.cleanup()
