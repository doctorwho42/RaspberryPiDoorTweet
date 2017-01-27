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

filename = '/home/john/pythoncode/getip/ipstate.p'

#function to read current ip address
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

#Read current state from computer
ipstate = get_ip_address('wlan0')

#open pickle
fileObject = open(filename,'r')
#read pickle for Last IP	
lastip = pickle.load(fileObject)
print(lastip)
fileObject.close()


if lastip != ipstate:

	msg = MIMEMultipart()
	msg['From'] = 'mitersdoor@gmail.com'
	msg['To'] = 'mitersdoor@gmail.com'
	msg['Subject'] = 'IP Check: %s' % ipstate


	s = smtplib.SMTP('smtp.gmail.com:587')
	s.ehlo()
	s.starttls()
	s.login('mitersdoor@gmail.com','[robot1663]')
	s.sendmail('mitersdoor@gmail.com', 'mitersdoor@gmail.com', 		msg.as_string())
	s.quit()

lastip = ipstate

#open pickle
fileObject = open(filename,'wb')
pickle.dump(lastip,fileObject)
fileObject.close()

