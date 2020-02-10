


# -*- coding: utf-8 -*-

"""
Created on 24.12.19

:author: Bologov V.A.
:email: vasiliybologov@gmail.com

"""

import smtplib
from email.mime.text import MIMEText
import textile
import imaplib
import email
import time
import datetime

# SMTP-сервер
server = "104.210.52.21"
port = 25

# user_name = "artur.b@xor.ai"


subj = 'test mail from MY SMTP'

text = " TEst test test test"
text = textile.textile(text)

s = smtplib.SMTP(server, port)

s.ehlo()
s.starttls()

you = 'vasilii.b@xor.ai'
#you = "vasoadmin@xorai.tech"

to = "vasilii.b@xor.ai"

# формирование сообщения
# msg = MIMEText(text, 'plain', 'cp1251')
msg = MIMEText(text, 'html', 'utf-8')
msg['Subject'] = subj
msg['From'] = you
msg['To'] = 'vasilii.b@xor.ai'

# отправка

#s.login("salesServer2", "salesServer2")

"""    try:
    s.login(user_name, user_passwd)
    #print(" Логин и пароль верны")
except:
    print(" Ошибка Логина или пароля")"""

# s.sendmail(you, 'seth.d@xor.ai', msg.as_string())
#s.sendmail(you, to, msg.as_string())

s.send_message(msg)

w = 0

while w < 3:
    s.sendmail(you, 'anton.c@xorte.ch', msg.as_string())
    w+=1










