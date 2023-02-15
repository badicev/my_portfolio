import smtplib, ssl
import os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "basakstreamlit@gmail.com"
    pw = os.getenv("PASSWORD")
    receiver = "basakstreamlit@gmail.com"
    context = ssl.create_default_context()
#     message = """\
# Subject:Hello!
# How are you?"""
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, pw)
        server.sendmail(username, receiver, message)

