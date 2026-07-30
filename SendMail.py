import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

def SendMail(receiver, subject, body, attachment):

    sender = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    msg = EmailMessage()

    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    msg.set_content(body)

    with open(attachment, "rb") as f:
        file_data = f.read()
        file_name = os.path.basename(attachment)

    msg.add_attachment(
        file_data,
        maintype="application",
        subtype="octet-stream",
        filename=file_name
    )

    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp.login(sender, password)
    smtp.send_message(msg)
    smtp.quit()

    print("Mail Sent Successfully")