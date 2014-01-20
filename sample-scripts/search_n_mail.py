#!/usr/bin/python
###############################################
###       Search a pattern from a log       ###
###############################################
import sys
import smtplib

sender = 'yoursearchscript@fromyourdomain.com'
#receivers has to be in the list
receivers = []
receivers.append(sys.argv[1])
#If you want to add more receivers you can append their email-id' to the above receivers list, receivers.append('email-id')
search_word = "dhcpd"

def sendmail(body):
    #Code to send a mail goes here
    message = "Subject: SMTP E-mail Testing"+"\n"+ str(body)
    print message
    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receivers, message)         
        print "Successfully sent email"
    except:
        print "Error: unable to send email"

#Infinite Loop :)
while True:
    try:
        info = str(sys.stdin.readline())
        if search_word in info: 
            #print info
            sendmail(info)
    except KeyboardInterrupt:
        print "\n Aborting!"
        exit
    if not info:
        break
