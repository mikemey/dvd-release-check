import os

SMTPserver = os.environ['DRC_SMTP_SERVER']
sender = os.environ['DRC_SENDER']
destination = [os.environ['DRC_DESTINATION']]

USERNAME = os.environ['DRC_USERNAME']
PASSWORD = os.environ['DRC_PASSWORD']

print "Sending email to: " + destination[0]
print "             via: " + SMTPserver
print "            from: " + sender
print "        gmx-user: " + USERNAME
print "         gmx-pwd: " + PASSWORD

exit(0)
