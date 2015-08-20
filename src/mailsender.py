def send(email_subject, email_content):
    global os
    smtp_server = os.environ['DRC_SMTP_SERVER']
    sender = os.environ['DRC_SENDER']
    destination = [os.environ['DRC_DESTINATION']]

    username = os.environ['DRC_USERNAME']
    password = os.environ['DRC_PASSWORD']

    # typical values for text_subtype are plain, html, xml
    text_subtype = 'plain'

    subject = email_subject
    content = email_content

    # print "subj: [%s]\ndata: [%s]" % (subject, content)

    import os

    # from smtplib import SMTP_SSL as SMTP       # this invokes the secure SMTP protocol (port 465, uses SSL)
    from smtplib import SMTP  # use this for standard SMTP protocol   (port 25, no encryption)
    from email.mime.text import MIMEText

    try:
        msg = MIMEText(content, text_subtype)
        msg['Subject'] = subject
        msg['From'] = sender  # some SMTP servers will do this automatically, not all

        conn = SMTP(smtp_server)
        conn.set_debuglevel(False)
        conn.login(username, password)
        try:
            print 'sending mail....'
            conn.sendmail(sender, destination, msg.as_string())
        finally:
            conn.close()
            return 0
    except Exception, exc:
        # sys.exit( "mail failed; %s" % str(exc) ) # give a error message
        print 'sending failed: %s' % str(exc)
        return 1
