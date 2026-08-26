# Day-25
'''
we want to send Automated email using python by add attcah files
'''

import smtplib
import email
import os

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders   # Added

# same include mail with subject code

From = "jagadeeshboyalla3384@gmail.com"
To = "jagadeeshsrkr3384@gmail.com"
Subject = "Email Automation Using Python - Single user attachment"
app_password = "vtwn grat hxat gokz"   # Replace with a new App Password
body = "In this project we will understand how python be useful in real world applications"
attachment = "simplemail.py"  # give your attachment

attach = attachment   # Added

msg = MIMEMultipart()
msg["From"] = From
msg["To"] = To
msg["Subject"] = Subject
msg.attach(MIMEText(body))

# now we add file content

part = MIMEBase('application', 'octet-stream')
part.set_payload(open(attach, 'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition','attachment; filename="%s"' % (os.path.basename(attach)))

msg.attach(part)
text = msg.as_string()

# start server communication

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(From, app_password)
server.sendmail(From, To, text)
print("Mail Sent")
server.quit()


# bulk mail --> wednesday use control block


