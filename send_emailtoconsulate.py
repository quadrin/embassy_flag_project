import smtplib as smt
import time

import email_scraping
import config
from email_scraping import email_list

def send_email(subject, msg):
    try: #trying to connect to gmail server
        server = smt.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, EMAIL_ADDRESS_RECIPIENT, message)
        print("Email sent.")
        server.quit()
    except:
        print("Email failed to send.")

subject = "Flag"
msg = """[Email message here!!!!!!!]"""

for i in range(len(email_list)):
    EMAIL_ADDRESS_RECIPIENT = email_list[i]
    send_email(subject, msg)
    time.sleep(3)
