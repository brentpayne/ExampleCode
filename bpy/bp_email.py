#!python
'''
Example code from the internet for emailing in python
http://www.blog.pythonlibrary.org/2010/05/14/how-to-send-email-with-python/

Here you have placed a basic e-mail in message, using a triple quote, taking care to format the headers correctly. An e-mails requires a From, To, and Subject header, separated from the body of the e-mail with a blank line.
'''
import smtplib
import string
import os
 
def simple_email():
    SUBJECT = "Test email from Python"
    TO = "mike@mydomain.com"
    FROM = "python@mydomain.com"
    text = "blah blah blah"
    BODY = string.join((
            "From: %s" % FROM,
            "To: %s" % TO,
            "Subject: %s" % SUBJECT ,
            "",
            text
            ), "\r\n")
    server = smtplib.SMTP(HOST)
    server.sendmail(FROM, [TO], BODY)
    server.quit()
#Another simple mail example
#!/usr/bin/python

import smtplib

sender = 'from@fromdomain.com'
receivers = ['to@todomain.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""
def another_simple_email(sender=sender, receivers=recievers, message=message):
    try:
       smtpObj = smtplib.SMTP('localhost')
       smtpObj.sendmail(sender, receivers, message)         
       print "Successfully sent email"
    except SMTPException:
        print "Error: unable to send email"


import os 
from email import Encoders
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart
from email.Utils import formatdate
 
#filePath = r'\\some\path\to\a\file'
 
def sendEmailWithAttachment(TO = "mike@mydomain.com",
              FROM="support@mydomain.com", filepath=None):
    HOST = "mail.mydomain.com"
 
    msg = MIMEMultipart()
    msg["From"] = FROM
    msg["To"] = TO
    msg["Subject"] = "You've got mail!"
    msg['Date']    = formatdate(localtime=True)
 
    # attach a file
    part = MIMEBase('application', "octet-stream")
    part.set_payload( open(filePath,"rb").read() )
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(filePath))
    msg.attach(part)
 
    server = smtplib.SMTP(HOST)
    # server.login(username, password)  # optional
 
    try:
        failed = server.sendmail(FROM, TO, msg.as_string())
        server.close()
    except Exception, e:
        errorMsg = "Unable to send email. Error: %s" % str(e)

 

if __name__ == "__main__":
    print 'This is an example code file'
