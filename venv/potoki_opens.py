

# -*- coding: utf-8 -*-

"""
Created on 24.12.19

:author: Bologov V.A.
:email: vasiliybologov@gmail.com

"""




import textile
import base64
import codecs
import imaplib
import email
import urllib.request
import socket
import smtplib
import re
from threading import Thread
import requests
import time
import datetime
import os


senders = ['anton.c@xorai.tech', 'anton.ce@xorai.tech', 'anton.c@xorte.ch', 'anton.ce@xorte.ch', 'ernest.s@xorai.tech', 'ernest.sv@xorai.tech', 'ernest.s@xorte.ch', 'ernest.sv@xorte.ch', 'patrisia.g@xorai.tech', 'patrisia.gh@xorai.tech', 'patrisia.g@xorte.ch', 'patrisia.gh@xorte.ch', 'eugen.p@xorai.tech', 'eugen.po@xorai.tech', 'eugen.p@xorte.ch', 'eugen.po@xorte.ch', 'vlad.f@xorai.tech', 'vlad.fo@xorai.tech', 'vlad.f@xorte.ch', 'vlad.fo@xorte.ch', 'victoria.s@xorai.tech', 'victoria.se@xorai.tech', 'victoria.s@xorte.ch', 'victoria.se@xorte.ch', 'dmitrii.c@xorai.tech', 'dmitrii.ca@xorai.tech', 'dmitrii.c@xorte.ch', 'dmitrii.ca@xorte.ch', 'mihai.c@xorai.tech', 'mihai.ci@xorai.tech', 'mihai.c@xorte.ch', 'mihai.ci@xorte.ch', 'efim.s@xorai.tech', 'efim.sa@xorai.tech', 'efim.s@xorte.ch', 'efim.sa@xorte.ch', 'mihaela.v@xorai.tech', 'mihaela.vi@xorai.tech', 'mihaela.v@xorte.ch', 'mihaela.vi@xorte.ch', 'victor.z@xorai.tech', 'victor.za@xorai.tech', 'victor.z@xorte.ch', 'victor.za@xorte.ch', 'anna.v@xorai.tech', 'anna.va@xorai.tech', 'anna.v@xorte.ch', 'anna.va@xorte.ch', 'aurel.u@xorai.tech', 'aurel.un@xorai.tech', 'aurel.u@xorte.ch', 'aurel.un@xorte.ch', 'vladislav.z@xorai.tech', 'vladislav.za@xorai.tech', 'vladislav.z@xorte.ch', 'vladislav.za@xorte.ch', 'xenia.p@xorai.tech', 'xenia.pe@xorai.tech', 'xenia.p@xorte.ch', 'xenia.pe@xorte.ch', 'gleb.b@xorai.tech', 'gleb.bo@xorai.tech', 'Gleb.b@xorte.ch', 'gleb.bo@xorte.ch', 'rodion.p@xorai.tech', 'rodion.pa@xorai.tech', 'rodion.p@xorte.ch', 'rodion.pa@xorte.ch', 'vsevolod.g@xorai.tech', 'vsevolod.gh@xorai.tech', 'vsevolod.g@xorte.ch', 'vsevolod.gh@xorte.ch', 'george.o@xorai.tech', 'george.oj@xorai.tech', 'george.o@xorte.ch', 'george.oj@xorte.ch', 'nelly.p@xorai.tech', 'nelly.pa@xorai.tech', 'nelly.p@xorte.ch', 'nelly.pa@xorte.ch', 'dima.n@xorai.tech', 'dima.na@xorai.tech', 'dima.n@xorte.ch', 'dima.na@xorte.ch', 'dorin.g@xorai.tech', 'dorin.go@xorai.tech', 'dorin.g@xorte.ch', 'dorin.go@xorte.ch', 'daniel.c@xorai.tech', 'daniel.co@xorai.tech', 'daniel.c@xorte.ch', 'daniel.co@xorte.ch', 'dan.m@xorai.tech', 'dan.mo@xorai.tech', 'dan.m@xorte.ch', 'dan.mo@xorte.ch', 'alevtina.m@xorai.tech', 'alevtina.m@xorte.ch']



def opener(user):
    mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    # mail.login(user, passwd)
    mail.login(user, 'Superxor42')
    mail.list()
    mail.select("INBOX", readonly=False)
    result, data = mail.search(None, 'UNSEEN')     #mail.search(None, "ALL")
    ids = data[0]
    id_list = ids.split()
    #print(id_list)
    #print(str(len(id_list)))
    data_list = []
    for mel in id_list:
        data_dict = {}
        #print(mel)
        mel = mel.decode('utf-8')
        #print(mel)
        _, response = mail.fetch(mel, '(RFC822)')
        #print(response)

        """html = response[0][1].decode('utf-8')
        email2_message = email.message_from_string(html)
        data_dict['mail_to'] = email2_message['To']
        data_dict['mail_subject'] = email2_message['Subject']
        data_dict['mail_from'] = email.utils.parseaddr(email2_message['From'])
        data_dict['body'] = email2_message.get_payload()
        print(data_dict)"""


        #print(len(response))
        if len(response) != 1:
            #print(response)
            g = response[0][1].decode("UTF-8")
            #print(g)
            # g = response[0][1]
            g = g.split(' ')
            #print(len(g))
            #print(len(g[len(g) - 1]))

            if len(g[len(g) - 1]) > 200:
                #print("---------------записано")
                #print(g[len(g) - 1])

                ba = g[len(g) - 1]
                #print(ba)
                ba = ba.split("\r\n")
                #print(ba)
                #print('baba')
                x = 2
                baba = ''
                while x < len(ba):
                    baba = baba + ba[x] + "\r\n"
                    x += 1

                #print(baba)

                #print("try")

                #print(base64.b64decode(baba).decode("UTF-8"))

                norm = base64.b64decode(baba).decode("UTF-8")

                #print(norm)

                norm = norm.split('"')
                xex = norm[len(norm) - 12]
                # xex = xex + "\n"  # только для записи в файл
                #print(xex)

                try:
                    r = urllib.request.urlopen(xex)
                    #print(" ---------------------- open")
                except:
                    print("Error")

                data_list.append(xex)
    #print(data_list)
    mail.expunge()
    file = open(user + '.orrrg', "w")
    file.writelines(data_list)
    file.close()
"""
w = 0
while w < 100000:
    for us in senders:
        print("open " + us)

        try:
            opener(us)
        except:
            print("error open  " + us)
    w += 1"""






t_ = str(datetime.datetime.today())
print(t_)




w = 0
while w < 1000000000:
    us = 0
    while us < len(senders):
        t = us
        jo = ''
        print("open first 10 ")
        try:
            jo = senders[t]
            print(jo)
            thread1 = Thread(target=opener, args=(jo, ), daemon=True)
            t+=1
        except:
            print("Error 1 from 10")
        try:
            jo = senders[t]
            print(jo)
            thread2 = Thread(target=opener, args=(jo, ), daemon=True)
            t += 1
        except:
            print("Error 2 from 10")
        try:
            jo = senders[t]
            print(jo)
            thread3 = Thread(target=opener, args=(jo, ), daemon=True)
            t += 1
        except:
            print("Error 3 from 10")
        try:
            jo = senders[t]
            print(jo)
            thread4 = Thread(target=opener, args=(jo, ), daemon=True)
            t += 1
        except:
            print("Error 4 from 10")
        try:
            jo = senders[t]
            print(jo)
            thread5 = Thread(target=opener, args=(jo, ), daemon=True)
            t += 1
        except:
            print("Error 5 from 10")
        try:
            jo = senders[t]
            print(jo)
            thread6 = Thread(target=opener, args=(jo, ), daemon=True)
            t += 1
        except:
            print("Error 6 from 10")
        try:
            jo = senders[t]
            print(jo)
            thread7 = Thread(target=opener, args=(jo, ), daemon=True)
            t += 1
        except:
            print("Error 7 from 10")
        try:
            jo = senders[t]
            print(jo)
            thread8 = Thread(target=opener, args=(jo, ), daemon=True)
            t += 1
        except:
            print("Error 8 from 10")
        try:
            jo = senders[t]
            print(jo)
            thread9 = Thread(target=opener, args=(jo, ), daemon=True)
            t += 1
        except:
            print("Error 9 from 10")
        try:
            jo = senders[t]
            print(jo)
            thread10 = Thread(target=opener, args=(jo, ), daemon=True)
            t += 1
        except:
            print("Error 10 from 10")
        us = t



        try:
            try:
                thread1.start()
            except:
                print("error start  1")
            try:
                thread2.start()
            except:
                print("error start  2")
            try:
                thread3.start()
            except:
                print("error start  3")
            try:
                thread4.start()
            except:
                print("error start  4")
            try:
                thread5.start()
            except:
                print("error start  5")
            try:
                thread6.start()
            except:
                print("error start  6")
            try:
                thread7.start()
            except:
                print("error start  7")
            try:
                thread8.start()
            except:
                print("error start  8")
            try:
                thread9.start()
            except:
                print("error start  9")
            try:
                thread10.start()
            except:
                print("error start  10")

            try:
                thread1.join()
                thread2.join()
                thread3.join()
                thread4.join()
                thread5.join()
                thread6.join()
                thread7.join()
                thread8.join()
                thread9.join()
                thread10.join()
            except:
                print("error close ")
        except:
            print("global error open  ")
    w += 1












t = str(datetime.datetime.today())
print(t_, t)