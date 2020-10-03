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
msg = """Dear representitives,

I am a 16 year old geography buff and have recently started collecting flags. I do not have your country's flag, but would you be so kind to send one my way? I would be very happy with any sort of flag. Thank you very much-- wishing for peace and prosperity to your country!

Regards,

Alexander


24 Avon Road
Hewlett, New York
Nassau County 11557
United States of America"""

for i in range(len(email_list)):
    EMAIL_ADDRESS_RECIPIENT = email_list[i]
    send_email(subject, msg)
    time.sleep(3)
