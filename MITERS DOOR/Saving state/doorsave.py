#!/usr/bin/env python
import RPi.GPIO as GPIO
import datetime
import time
import sys
import csv

Date = '{:%Y-%m-%d%H:%M:%S}'.format(datetime.datetime.now())

csvdate = '{:%Y-%m}'.format(datetime.datetime.now())

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

input_state = GPIO.input(18)

if input_state == False:
        #Door is open
        Doorstate = 'open'

elif input_state == True:
        #Door is closed
        Doorstate = 'closed'
csvfilename ='/home/pi/doortweeter/' + 'doorstate_' + csvdate + '.csv'


with open(csvfilename, 'ab') as csvFile:
        appender = csv.writer(csvFile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        appender.writerow([csvdate, Doorstate])
