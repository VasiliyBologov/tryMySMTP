
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


senders = ['anton.c@xorai.tech', 'anton.ce@xorai.tech', 'anton.c@xorte.ch', 'anton.ce@xorte.ch', 'ernest.s@xorai.tech', 'ernest.sv@xorai.tech', 'ernest.s@xorte.ch', 'ernest.sv@xorte.ch', 'patrisia.g@xorai.tech', 'patrisia.gh@xorai.tech', 'patrisia.g@xorte.ch', 'patrisia.gh@xorte.ch', 'eugen.p@xorai.tech', 'eugen.po@xorai.tech', 'eugen.p@xorte.ch', 'eugen.po@xorte.ch', 'vlad.f@xorai.tech', 'vlad.fo@xorai.tech', 'vlad.f@xorte.ch', 'vlad.fo@xorte.ch', 'victoria.s@xorai.tech', 'victoria.se@xorai.tech', 'victoria.s@xorte.ch', 'victoria.se@xorte.ch', 'dmitrii.c@xorai.tech', 'dmitrii.ca@xorai.tech', 'dmitrii.c@xorte.ch', 'dmitrii.ca@xorte.ch', 'mihai.c@xorai.tech', 'mihai.ci@xorai.tech', 'mihai.c@xorte.ch', 'mihai.ci@xorte.ch', 'efim.s@xorai.tech', 'efim.sa@xorai.tech', 'efim.s@xorte.ch', 'efim.sa@xorte.ch', 'mihaela.v@xorai.tech', 'mihaela.vi@xorai.tech', 'mihaela.v@xorte.ch', 'mihaela.vi@xorte.ch', 'victor.z@xorai.tech', 'victor.za@xorai.tech', 'victor.z@xorte.ch', 'victor.za@xorte.ch', 'anna.v@xorai.tech', 'anna.va@xorai.tech', 'anna.v@xorte.ch', 'anna.va@xorte.ch', 'aurel.u@xorai.tech', 'aurel.un@xorai.tech', 'aurel.u@xorte.ch', 'aurel.un@xorte.ch', 'vladislav.z@xorai.tech', 'vladislav.za@xorai.tech', 'vladislav.z@xorte.ch', 'vladislav.za@xorte.ch', 'xenia.p@xorai.tech', 'xenia.pe@xorai.tech', 'xenia.p@xorte.ch', 'xenia.pe@xorte.ch', 'gleb.b@xorai.tech', 'gleb.bo@xorai.tech', 'Gleb.b@xorte.ch', 'gleb.bo@xorte.ch', 'rodion.p@xorai.tech', 'rodion.pa@xorai.tech', 'rodion.p@xorte.ch', 'rodion.pa@xorte.ch', 'vsevolod.g@xorai.tech', 'vsevolod.gh@xorai.tech', 'vsevolod.g@xorte.ch', 'vsevolod.gh@xorte.ch', 'george.o@xorai.tech', 'george.oj@xorai.tech', 'george.o@xorte.ch', 'george.oj@xorte.ch', 'nelly.p@xorai.tech', 'nelly.pa@xorai.tech', 'nelly.p@xorte.ch', 'nelly.pa@xorte.ch', 'dima.n@xorai.tech', 'dima.na@xorai.tech', 'dima.n@xorte.ch', 'dima.na@xorte.ch', 'dorin.g@xorai.tech', 'dorin.go@xorai.tech', 'dorin.g@xorte.ch', 'dorin.go@xorte.ch', 'daniel.c@xorai.tech', 'daniel.co@xorai.tech', 'daniel.c@xorte.ch', 'daniel.co@xorte.ch', 'dan.m@xorai.tech', 'dan.mo@xorai.tech', 'dan.m@xorte.ch', 'dan.mo@xorte.ch', 'alevtina.m@xorai.tech', 'alevtina.m@xorte.ch']

coint_send = 0

coint_reed = 0


def end_step():
    # SMTP-сервер
    # server = "smtp.gmail.com"
    # port = 587
    # user_name = "artur.b@xor.ai"

    # SMTP-сервер
    server = "smtp.sendgrid.net"  #
    port = 587  # тут должен быть сендгрид
    # если сендгрид то логин пароль вот эти

    user_name = 'apikey'
    user_passwd = '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'

    # user_passwd = "Superxor42"

    subj = 'степ разогрева закончен'

    text = " степ разогрева закончен, запустите заново"
    text = textile.textile(text)

    s = smtplib.SMTP(server, port)
    s.ehlo()
    s.starttls()

    you = 'vasilii.b@getxor.com'


    # формирование сообщения
    # msg = MIMEText(text, 'plain', 'cp1251')
    msg = MIMEText(text, 'html', 'utf-8')
    msg['Subject'] = subj
    msg['From'] = you
    msg['To'] = 'seth.d@xor.ai'

    # отправка

    try:
        s.login(user_name, user_passwd)
        #print(" Логин и пароль верны")
    except:
        print(" Ошибка Логина или пароля")

    try:
        s.sendmail(you, 'seth.d@xor.ai', msg.as_string())
        # s.send_message(msg)
        # print(senders[z] + "  Письма отправлены")
    except:
        print(senders[z] + "   Ошибка отправки!")




def runsend():
    coint_sender = 0
    # SMTP-сервер
    # server = "smtp.gmail.com"
    # port = 587
    # user_name = "artur.b@xor.ai"

    # SMTP-сервер
    server = "smtp.sendgrid.net"  #
    port = 587  # тут должен быть сендгрид
    # если сендгрид то логин пароль вот эти

    user_name = 'apikey'
    user_passwd = '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'

    # user_passwd = "Superxor42"

    subj = 'Merry X-Mas and Happy Holidays sendgrid'

    text = "Hi , \n I'm reaching out to set up a quick call to discuss how XOR can help you automate your communications to go from “cold candidate outreach” to “interview scheduled” in 5 minutes.\n\nGiven your role, In assume that shortening time-to-hire and increasing hiring efficiency is a priority.\n   XOR is helping employers like McDonald’s, IKEA, and Manpower Group hire faster by automating text messages to announce new job postings, screen candidates,\nand schedule interviews, so your recruiting team is only speaking with qualified candidates.\n\nWe also integrate with 30 different ATS’s and job boards and offer the best support and implementation in the industry.\n\nDo you have time for a quick call to discuss how XOR can help you automate your recruiting communications?\n\n\n\n\n\nWith best regards,\n"

    text = textile.textile(text)

    s = smtplib.SMTP(server, port)
    s.ehlo()
    s.starttls()

    """try:
        s.login(user_name, user_passwd)
        #print(" Логин и пароль верны")
    except:
        print(" Ошибка Логина или пароля")"""

    z = 0
    while z < len(senders):
        print(str(z+1) + ' ' + senders[z] + '  send emails ....')
        s = smtplib.SMTP(server, port)
        s.ehlo()
        s.starttls()

        try:
            s.login(user_name, user_passwd)
            # print(" Логин и пароль верны")
        except:
            print(" Ошибка Логина или пароля")
        i = 0
        while i < len(senders):
            #print(" -------   try send to " + senders[i])

            if i != z:
                # you = 'vasilii.b@getxor.com'
                you = senders[i]

                # формирование сообщения
                # msg = MIMEText(text, 'plain', 'cp1251')
                msg = MIMEText(text, 'html', 'utf-8')
                msg['Subject'] = subj
                msg['From'] = senders[z]
                msg['To'] = you

                # отправка

                try:
                    s.sendmail(senders[z], you, msg.as_string())
                    coint_sender += 1
                    # s.send_message(msg)
                    #print(senders[z] + "  Письма отправлены")
                except:
                    print(senders[z] + "   Ошибка отправки!")
            i += 1

        s.quit()
        z += 1
    print(coint_sender)

def runresend():
    coint_sender = 0
    # SMTP-сервер
    # server = "smtp.gmail.com"
    # port = 587
    # user_name = "artur.b@xor.ai"

    # SMTP-сервер
    server = "smtp.sendgrid.net"  #
    port = 587  # тут должен быть сендгрид
    # если сендгрид то логин пароль вот эти

    user_name = 'apikey'
    user_passwd = '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'

    # user_passwd = "Superxor42"

    subj = '[RE]Merry X-Mas and Happy Holidays sendgrid'

    text = "Hi , \n I'm reaching out to set up a quick call to discuss how XOR can help you automate your communications to go from “cold candidate outreach” to “interview scheduled” in 5 minutes.\n\nGiven your role, In assume that shortening time-to-hire and increasing hiring efficiency is a priority.\n   XOR is helping employers like McDonald’s, IKEA, and Manpower Group hire faster by automating text messages to announce new job postings, screen candidates,\nand schedule interviews, so your recruiting team is only speaking with qualified candidates.\n\nWe also integrate with 30 different ATS’s and job boards and offer the best support and implementation in the industry.\n\nDo you have time for a quick call to discuss how XOR can help you automate your recruiting communications?\n\n\n\n\n\nWith best regards,\n"

    text = textile.textile(text)

    s = smtplib.SMTP(server, port)
    s.ehlo()
    s.starttls()

    """try:
        s.login(user_name, user_passwd)
        #print(" Логин и пароль верны")
    except:
        print(" Ошибка Логина или пароля")"""

    z = 0
    while z < len(senders):
        print(str(z+1) + ' ' + senders[z] + '  send emails ....')
        s = smtplib.SMTP(server, port)
        s.ehlo()
        s.starttls()

        try:
            s.login(user_name, user_passwd)
            # print(" Логин и пароль верны")
        except:
            print(" Ошибка Логина или пароля")
        i = 0
        while i < len(senders):
            #print(" -------   try send to " + senders[i])

            if i != z:
                # you = 'vasilii.b@getxor.com'
                you = senders[i]

                # формирование сообщения
                # msg = MIMEText(text, 'plain', 'cp1251')
                msg = MIMEText(text, 'html', 'utf-8')
                msg['Subject'] = subj
                msg['From'] = senders[z]
                msg['To'] = you

                # отправка

                try:
                    s.sendmail(senders[z], you, msg.as_string())
                    coint_sender += 1
                    # s.send_message(msg)
                    #print(senders[z] + "  Письма отправлены")
                except:
                    print(senders[z] + "   Ошибка отправки!")
            i += 1
        s.quit()
        z += 1
    print(coint_sender)


def readspam(username, password, sender_of_interest=None):
    # Login to INBOX
    imap = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    imap.login(username, password)
    #print(imap.list())
    imap.select('[Gmail]/Spam')
    # Use search(), not status()
    # Print all unread messages from a certain sender of interest
    if sender_of_interest:
        status, response = imap.uid('search', None, 'UNSEEN', 'FROM {0}'.format(sender_of_interest))
    else:
        status, response = imap.uid('search', None, 'UNSEEN')
    if status == 'OK':
        unread_msg_nums = response[0].split()
    else:
        unread_msg_nums = []
    data_list = []
    for e_id in unread_msg_nums:
        data_dict = {}
        e_id = e_id.decode('utf-8')
        _, response = imap.uid('fetch', e_id, '(RFC822)')
        html = response[0][1].decode('utf-8')
        email2_message = email.message_from_string(html)
        data_dict['mail_to'] = email2_message['To']
        data_dict['mail_subject'] = email2_message['Subject']
        data_dict['mail_from'] = email.utils.parseaddr(email2_message['From'])
        data_dict['body'] = email2_message.get_payload()
        data_list.append(data_dict)
    print("Read emails from SPAM from " + username + ' ...')

def readinbox(username, password, sender_of_interest=None):
    # Login to INBOX
    imap = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    imap.login(username, password)
    #print(imap.list())
    imap.select('INBOX')
    # Use search(), not status()
    # Print all unread messages from a certain sender of interest
    if sender_of_interest:
        status, response = imap.uid('search', None, 'UNSEEN', 'FROM {0}'.format(sender_of_interest))
    else:
        status, response = imap.uid('search', None, 'UNSEEN')
    if status == 'OK':
        unread_msg_nums = response[0].split()
    else:
        unread_msg_nums = []
    data_list = []
    for e_id in unread_msg_nums:
        data_dict = {}
        e_id = e_id.decode('utf-8')
        _, response = imap.uid('fetch', e_id, '(RFC822)')
        html = response[0][1].decode('utf-8')
        email2_message = email.message_from_string(html)
        data_dict['mail_to'] = email2_message['To']
        data_dict['mail_subject'] = email2_message['Subject']
        data_dict['mail_from'] = email.utils.parseaddr(email2_message['From'])
        data_dict['body'] = email2_message.get_payload()
        data_list.append(data_dict)
    print("Read emails from INBOX from " + username + ' ...')


def not_spam(username):
    mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    mail.login(username, 'Superxor42')

    while True:
        mail.list()
        mail.select("[Gmail]/Spam", readonly=False)
        result, data = mail.search(None, "ALL")
        ids = data[0]
        id_list = ids.split()
        #print(id_list)
        for mail_id in id_list:
            #print(mail_id)
            no_spam = mail.store(mail_id, '+FLAGS', '$NotPhishing')
            if no_spam[0] == 'OK':
                #print("ok1")
                delete_res = mail.store(mail_id, '+FLAGS', '$NotPhishing')
            # no_spam = mail.store(mail_id, '+FLAGS', '$NotPhishing')
            copy_res = mail.copy(mail_id, 'INBOX')
            if copy_res[0] == 'OK':
                #print("ok2")
                delete_res = mail.store(mail_id, '+FLAGS', '$NotPhishing')

        mail.expunge()
        mail.list()
        mail.select("[Gmail]/Spam", readonly=False)
        result, data = mail.search(None, "ALL")
        ids = data[0]
        id_list = ids.split()
        print(id_list)
        mail.expunge()
        if id_list == []:
            break

    print("end not spam  " + username)


qq = 0

while qq < 3:
    t_ = str(datetime.datetime.today())
    print(t_)
    try:
        print("send try")
        #runsend()
    except:
        print("send error")

    t = str(datetime.datetime.today())
    print(t_, t)
    print("end send")

    w = 0
    while w < len(senders):
        try:
            print("try no spam " + senders[w])
            not_spam(senders[w])
        except:
            print(senders[w] + "   пидор")
        w += 1

    t = str(datetime.datetime.today())
    print(t_, t)
    print("end not to spam")

    """e = 0

    while e < len(senders):
        print(e)
        print(senders[e])
        try:
            #readspam(senders[e], 'Superxor42')
            readinbox(senders[e], 'Superxor42')
        except:
            print("пидор")

        e += 1"""

    try:
        print(" RE send try")
        #runresend()
    except:
        print(" RE send error")

    t = str(datetime.datetime.today())
    print(t_, t)
    print("end send")
    end_step()
    print("end all")
    t = str(datetime.datetime.today())
    print(t_, t)

    print('отправлено писем :   ')


    qq+=1