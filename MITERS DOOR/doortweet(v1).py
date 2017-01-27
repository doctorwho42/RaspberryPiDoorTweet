#!/usr/bin/env python
import RPi.GPIO as GPIO
import datetime
import time
import sys
from twython import Twython
CONSUMER_KEY = 'XXXXX'
CONSUMER_SECRET = 'XXXXX'
ACCESS_KEY = 'XXXXX'
ACCESS_SECRET = 'XXXXX'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

input_state = GPIO.input(18)
if input_state == False:
        api.update_status(status='MITERS door is open! {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
        time.sleep(0.2)
elif input_state == True:
        api.update_status(status='MITERS door is closed! {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
        time.sleep(0.2)
