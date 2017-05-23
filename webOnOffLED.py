#!/usr/bin/python

import sys
import RPi.GPIO as GPIO ## Import GPIO library
GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(7, GPIO.OUT) ## Setup GPIO Pin 7 to OUT

#getting the input parms
argsLen = len(sys.argv)
if argsLen == 2:
  if sys.argv[1] == "on":
    #Turn ON
    print("Turning LED ON")
    GPIO.output(7,True)
  elif sys.argv[1] == "off":
    #Turn OFF
    print("Turning LED OFF")
    GPIO.output(7,False)
