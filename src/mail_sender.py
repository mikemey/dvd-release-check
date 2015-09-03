import os
from smtplib import SMTP
from email.mime.text import MIMEText

from drc_commons import logger


def send(email_subject, email_content):
    if 'DRC_SMTP_SERVER' not in os.environ:
        logger.error("email variables not set!")
        return 1

    smtp_server = os.environ['DRC_SMTP_SERVER']
    sender = os.environ['DRC_SENDER']
    destination = [os.environ['DRC_DESTINATION']]

    username = os.environ['DRC_USERNAME']
    password = os.environ['DRC_PASSWORD']

    try:
        text_subtype = 'html'
        msg = MIMEText(email_content, text_subtype)
        msg['Subject'] = email_subject
        msg['From'] = sender

        conn = SMTP(smtp_server)
        conn.set_debuglevel(False)
        conn.login(username, password)
        try:
            logger.info('sending mail....')
            conn.sendmail(sender, destination, msg.as_string())
        finally:
            conn.close()
            return 0
    except Exception, exc:
        logger.info('sending failed: %s' % str(exc))
        return 1
