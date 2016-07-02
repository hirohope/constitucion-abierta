# -*- coding: UTF-8 -*-.
import smtplib

from email.mime.text import MIMEText
from email.header import Header


gmail_user = 'constitucionabierta@gmail.com'
gmail_password = 'por la puta madre!'


subject = "Hemos recibido una nueva acta"

message = """
Hola %s,

Hay una nueva acta para revisar.

Debes revisar el acta %s.

Esta es la acta que debes anonimizar %s
En este enlace debes subir la acta anonimizada %s

Puedes entrar a este enlace para ver la lista de actas https://docs.google.com/spreadsheets/d/1vaM3a6djbwKsOwqVY5N1XTN0SjU-JnEO_vHC0iD6M-0/edit#gid=0

Recuerda que la acta %s es la que debes revisar.

Saludos
"""

def send_email(from_, to_, name, acta_number, direct_url, modify_url):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_password)

        formated_message = message % (name, acta_number, direct_url, modify_url, acta_number)
        formated_message = formated_message

        msg = MIMEText(formated_message, _charset="UTF-8")
        msg['Subject'] = Header(subject, "utf-8")
        server.sendmail(from_, to_, msg.as_string())
        server.close()
    except Exception as e:
        print from_, to_, name, acta_number
        print 'Something went wrong...'
        print e
