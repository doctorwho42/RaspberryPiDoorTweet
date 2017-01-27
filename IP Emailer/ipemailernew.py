#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import socket
import fcntl
import struct
import pickle
import smtplib # Import smtplib for the actual sending function
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

theip = get_ip_address('wlan0')

currentip = pickle.load(open("/home/pi/pythoncode/getip/ipstate.p","rb"))

if currentip != theip:

	msg = MIMEMultipart()
	msg['From'] = 'EMAIL@ADDRESS'
	msg['To'] = 'EMAIL@ADDRESS'
	msg['Subject'] = 'IP Check: %s' % j


	s = smtplib.SMTP('smtp.gmail.com:587')
	s.ehlo()
	s.starttls()
	s.login('EMAIL@ADDRESS','Password')
	s.sendmail('EMAIL@ADDRESS', 'EMAIL@ADDRESS', msg.as_string())
	s.quit()

currentip = theip

pickle.dump(currentstate, open("/home/pi/pythoncode/getip/ipstate.p", "wb"))

