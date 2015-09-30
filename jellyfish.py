#! /usr/bin/python
# License: Apache 2.0

import os
from daemon import Daemon

import RPi.GPIO as GPIO

import time
from time import gmtime, strftime
import threading
#import yaml
import requests, json



#High Res Timer

GPIO.setmode(GPIO.BCM)

SPICLK = 18 #17
SPIMISO = 23 #24
SPIMOSI = 24 #25
SPICS = 25 #27
mybutton = 40

runner = True
url = "https://api.travis-ci.org"

if __name__ == '__main__':

  # set up the SPI interface pins
  GPIO.setup(SPIMOSI, GPIO.OUT)
  GPIO.setup(SPIMISO, GPIO.IN)
  GPIO.setup(SPICLK, GPIO.OUT)
  GPIO.setup(SPICS, GPIO.OUT)

  try:
    while (runner == True):




      #Sleep
      time.sleep(.5) #set to whatever

  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print "\nKilling Thread..."
    runner = False
  print "Almost done."
  GPIO.cleanup()
  print "Done.\nExiting."
  exit();
