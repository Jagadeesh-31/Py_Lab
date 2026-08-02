import smtplib
import random,math

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email details
From = "jagadeeshboyalla3384@gmail.com"
To = "jagadeeshsrkr3384@gmail.com"
Subject = "New Automation Mail Request"

# Create message
msg = MIMEMultipart()
msg["From"] = From
msg["To"] = To
msg["Subject"] = Subject
otp = random.randint(1000,9999)
body = f"""Hope you are following the Python class.
Make sure to practice more.{otp}
"""

msg.attach(MIMEText(body))

# Convert message to string
text = msg.as_string()

# Connect to Gmail SMTP server
server = smtplib.SMTP("smtp.gmail.com", 587)

# Start encryption
server.starttls()

# Login
server.login(
    "jagadeeshboyalla3384@gmail.com",
    "vtwn grat hxat gokz")

# Send email
server.sendmail(From, To, text)

print("Mail Sent Successfully!")

# Close connection
server.quit()

print("Done")

# will give base digits

digits = '0123456789'
otp =""
for i in range(6):
    otp+=digits[math.floor(random.random()*10)]
    # print(otp)
msg.attach(MIMEText(body))

# Convert message to string
text = msg.as_string()

# Connect to Gmail SMTP server
server = smtplib.SMTP("smtp.gmail.com", 587)

# Start encryption
server.starttls()

# Login
server.login(
    "jagadeeshboyalla3384@gmail.com",
    "vtwn grat hxat gokz")

# Send email
server.sendmail(From, To, text)

print("Mail Sent Successfully!")

# Close connection
server.quit()

print("Done")

a = input("Enter OTP recived:")
if a==otp:
    print('Login Sucessful')
else:
    print('Unsucessfull')



