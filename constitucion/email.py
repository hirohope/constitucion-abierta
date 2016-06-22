# -*- coding: UTF-8 -*-.

import smtplib

gmail_user = 'constitucionabierta@gmail.com'
gmail_password = 'por la puta madre!'

message = """
Hola %s,

Hay una nueva acta para revisar.
Entra acá https://docs.google.com/spreadsheets/d/1vaM3a6djbwKsOwqVY5N1XTN0SjU-JnEO_vHC0iD6M-0/edit#gid=0

Debes revisar el acta %s.

Saludos
"""

def send_email(from_, to_, name, acta_number):

    try:  
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.sendmail(from_, to_, message % (name, acta_number)) 
        server.close()
    except Exception as e:
        print 'Something went wrong...'
        print e
