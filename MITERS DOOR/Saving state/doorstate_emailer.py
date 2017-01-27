#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import time
import sys
import csv
import smtplib # Import smtplib for the actual sending function
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

today=datetime.date.today()
first = today.replace(day=1)
lastMonth = first - datetime.timedelta(days=1)

csvdate = lastMonth.strftime("%Y-%m")  #'{:%Y-%m}'.format(datetime.datetime.now())
csvfilename = '/home/pi/doortweeter/' + 'doorstate_' + csvdate + '.csv'

print(csvfilename)

msg = MIMEMultipart()
msg['From'] = 'EMAIL@ADDRESS'
msg['To'] = 'EMAIL@ADDRESS'
msg['Subject'] = 'This Month’s Logs'

csvFile = open(csvfilename, 'rb')
thing = MIMEBase('application', 'octet-stream')
thing.set_payload(csvFile.read())
csvFile.close()
encoders.encode_base64(thing)
thing.add_header('Content-Disposition', 'attachement', filename='doorstate_' + csvdate + '.csv')

msg.attach(thing)

s = smtplib.SMTP('smtp.gmail.com:587')
s.ehlo()
s.starttls()
s.login('EMAIL@ADDRESS','PASSWORD')
s.sendmail('EMAIL@ADDRESS', 'EMAIL@ADDRESS', msg.as_string())
s.quit()
