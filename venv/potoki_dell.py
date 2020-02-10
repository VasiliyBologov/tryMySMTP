

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
import time
import datetime
import os


senders = ['anton.c@xorai.tech', 'anton.ce@xorai.tech', 'anton.c@xorte.ch', 'anton.ce@xorte.ch', 'ernest.s@xorai.tech', 'ernest.sv@xorai.tech', 'ernest.s@xorte.ch', 'ernest.sv@xorte.ch', 'patrisia.g@xorai.tech', 'patrisia.gh@xorai.tech', 'patrisia.g@xorte.ch', 'patrisia.gh@xorte.ch', 'eugen.p@xorai.tech', 'eugen.po@xorai.tech', 'eugen.p@xorte.ch', 'eugen.po@xorte.ch', 'vlad.f@xorai.tech', 'vlad.fo@xorai.tech', 'vlad.f@xorte.ch', 'vlad.fo@xorte.ch', 'victoria.s@xorai.tech', 'victoria.se@xorai.tech', 'victoria.s@xorte.ch', 'victoria.se@xorte.ch', 'dmitrii.c@xorai.tech', 'dmitrii.ca@xorai.tech', 'dmitrii.c@xorte.ch', 'dmitrii.ca@xorte.ch', 'mihai.c@xorai.tech', 'mihai.ci@xorai.tech', 'mihai.c@xorte.ch', 'mihai.ci@xorte.ch', 'efim.s@xorai.tech', 'efim.sa@xorai.tech', 'efim.s@xorte.ch', 'efim.sa@xorte.ch', 'mihaela.v@xorai.tech', 'mihaela.vi@xorai.tech', 'mihaela.v@xorte.ch', 'mihaela.vi@xorte.ch', 'victor.z@xorai.tech', 'victor.za@xorai.tech', 'victor.z@xorte.ch', 'victor.za@xorte.ch', 'anna.v@xorai.tech', 'anna.va@xorai.tech', 'anna.v@xorte.ch', 'anna.va@xorte.ch', 'aurel.u@xorai.tech', 'aurel.un@xorai.tech', 'aurel.u@xorte.ch', 'aurel.un@xorte.ch', 'vladislav.z@xorai.tech', 'vladislav.za@xorai.tech', 'vladislav.z@xorte.ch', 'vladislav.za@xorte.ch', 'xenia.p@xorai.tech', 'xenia.pe@xorai.tech', 'xenia.p@xorte.ch', 'xenia.pe@xorte.ch', 'gleb.b@xorai.tech', 'gleb.bo@xorai.tech', 'Gleb.b@xorte.ch', 'gleb.bo@xorte.ch', 'rodion.p@xorai.tech', 'rodion.pa@xorai.tech', 'rodion.p@xorte.ch', 'rodion.pa@xorte.ch', 'vsevolod.g@xorai.tech', 'vsevolod.gh@xorai.tech', 'vsevolod.g@xorte.ch', 'vsevolod.gh@xorte.ch', 'george.o@xorai.tech', 'george.oj@xorai.tech', 'george.o@xorte.ch', 'george.oj@xorte.ch', 'nelly.p@xorai.tech', 'nelly.pa@xorai.tech', 'nelly.p@xorte.ch', 'nelly.pa@xorte.ch', 'dima.n@xorai.tech', 'dima.na@xorai.tech', 'dima.n@xorte.ch', 'dima.na@xorte.ch', 'dorin.g@xorai.tech', 'dorin.go@xorai.tech', 'dorin.g@xorte.ch', 'dorin.go@xorte.ch', 'daniel.c@xorai.tech', 'daniel.co@xorai.tech', 'daniel.c@xorte.ch', 'daniel.co@xorte.ch', 'dan.m@xorai.tech', 'dan.mo@xorai.tech', 'dan.m@xorte.ch', 'dan.mo@xorte.ch', 'alevtina.m@xorai.tech', 'alevtina.m@xorte.ch']


def dellls(user):

    colvo = 0

    passwd = 'Superxor42'

    mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    mail.login(user, passwd)
    mail.list()

    mail.select("INBOX", readonly=False)
    result, data = mail.search(None, "ALL")
    ids = data[0]
    id_list = ids.split()
    # print(id_list)

    #print(id_list)
    #print(str(len(id_list)))
    for mail_id in id_list:
        print(mail_id)
        no_spam2 = mail.store(mail_id, '+FLAGS', '\Seen')
        no_spam = mail.store(mail_id, '+FLAGS', '\Deleted')

        if no_spam2[0] == 'OK':
            if no_spam[0] == 'OK':
                colvo += 1
                #print("ok1", end = '')
        """except:
            print("Error    " + user)"""
            #delete_res = mail.store(mail_id, '+FLAGS', '\Deleted')
        # no_spam = mail.store(mail_id, '+FLAGS', '$NotPhishing')
        """copy_res = mail.copy(mail_id, 'INBOX')
        if copy_res[0] == 'OK':
            print("ok2")
            delete_res = mail.store(mail_id, '+FLAGS', '$NotPhishing')"""

    print("прочитано и удалено   " + str(colvo) + "   писем в почте   " + user)
    mail.expunge()




t_ = str(datetime.datetime.today())
print(t_)

try:
    try:
        thread1 = Thread(target=dellls, args=('anton.c@xorai.tech',), daemon=True)

    except:
        print("Error anton.c@xorai.tech ")

    try:
        thread2 = Thread(target=dellls, args=('anton.ce@xorai.tech',), daemon=True)

    except:
        print("Error anton.ce@xorai.tech ")

    try:
        thread3 = Thread(target=dellls, args=('anton.c@xorte.ch',), daemon=True)

    except:
        print("Error anton.c@xorte.ch ")

    try:
        thread4 = Thread(target=dellls, args=('anton.ce@xorte.ch',), daemon=True)

    except:
        print("Error anton.ce@xorte.ch ")

    try:
        thread5 = Thread(target=dellls, args=('ernest.s@xorai.tech',), daemon=True)

    except:
        print("Error ernest.s@xorai.tech ")

    try:
        thread6 = Thread(target=dellls, args=('ernest.sv@xorai.tech',), daemon=True)

    except:
        print("Error ernest.sv@xorai.tech ")

    try:
        thread7 = Thread(target=dellls, args=('ernest.s@xorte.ch',), daemon=True)

    except:
        print("Error ernest.s@xorte.ch ")

    try:
        thread8 = Thread(target=dellls, args=('ernest.sv@xorte.ch',), daemon=True)

    except:
        print("Error ernest.sv@xorte.ch ")

    try:
        thread9 = Thread(target=dellls, args=('patrisia.g@xorai.tech',), daemon=True)

    except:
        print("Error patrisia.g@xorai.tech ")

    try:
        thread10 = Thread(target=dellls, args=('patrisia.gh@xorai.tech',), daemon=True)

    except:
        print("Error patrisia.gh@xorai.tech ")

    try:
        thread11 = Thread(target=dellls, args=('patrisia.g@xorte.ch',), daemon=True)

    except:
        print("Error patrisia.g@xorte.ch ")

    try:
        thread12 = Thread(target=dellls, args=('patrisia.gh@xorte.ch',), daemon=True)

    except:
        print("Error patrisia.gh@xorte.ch ")

    try:
        thread13 = Thread(target=dellls, args=('eugen.p@xorai.tech',), daemon=True)

    except:
        print("Error eugen.p@xorai.tech ")

    try:
        thread14 = Thread(target=dellls, args=('eugen.po@xorai.tech',), daemon=True)

    except:
        print("Error eugen.po@xorai.tech ")

    try:
        thread15 = Thread(target=dellls, args=('eugen.p@xorte.ch',), daemon=True)

    except:
        print("Error eugen.p@xorte.ch ")

    try:
        thread16 = Thread(target=dellls, args=('eugen.po@xorte.ch',), daemon=True)

    except:
        print("Error eugen.po@xorte.ch ")

    try:
        thread17 = Thread(target=dellls, args=('vlad.f@xorai.tech',), daemon=True)

    except:
        print("Error vlad.f@xorai.tech ")

    try:
        thread18 = Thread(target=dellls, args=('vlad.fo@xorai.tech',), daemon=True)

    except:
        print("Error vlad.fo@xorai.tech ")

    try:
        thread19 = Thread(target=dellls, args=('vlad.f@xorte.ch',), daemon=True)

    except:
        print("Error vlad.f@xorte.ch ")

    try:
        thread20 = Thread(target=dellls, args=('vlad.fo@xorte.ch',), daemon=True)

    except:
        print("Error vlad.fo@xorte.ch ")

    try:
        thread21 = Thread(target=dellls, args=('victoria.s@xorai.tech',), daemon=True)

    except:
        print("Error victoria.s@xorai.tech ")

    try:
        thread22 = Thread(target=dellls, args=('victoria.se@xorai.tech',), daemon=True)

    except:
        print("Error victoria.se@xorai.tech ")

    try:
        thread23 = Thread(target=dellls, args=('victoria.s@xorte.ch',), daemon=True)

    except:
        print("Error victoria.s@xorte.ch ")

    try:
        thread24 = Thread(target=dellls, args=('victoria.se@xorte.ch',), daemon=True)

    except:
        print("Error victoria.se@xorte.ch ")

    try:
        thread25 = Thread(target=dellls, args=('dmitrii.c@xorai.tech',), daemon=True)

    except:
        print("Error dmitrii.c@xorai.tech ")

    try:
        thread26 = Thread(target=dellls, args=('dmitrii.ca@xorai.tech',), daemon=True)

    except:
        print("Error dmitrii.ca@xorai.tech ")

    try:
        thread27 = Thread(target=dellls, args=('dmitrii.c@xorte.ch',), daemon=True)

    except:
        print("Error dmitrii.c@xorte.ch ")

    try:
        thread28 = Thread(target=dellls, args=('dmitrii.ca@xorte.ch',), daemon=True)

    except:
        print("Error dmitrii.ca@xorte.ch ")

    try:
        thread29 = Thread(target=dellls, args=('mihai.c@xorai.tech',), daemon=True)

    except:
        print("Error mihai.c@xorai.tech ")

    try:
        thread30 = Thread(target=dellls, args=('mihai.ci@xorai.tech',), daemon=True)

    except:
        print("Error mihai.ci@xorai.tech ")

    try:
        thread31 = Thread(target=dellls, args=('mihai.c@xorte.ch',), daemon=True)

    except:
        print("Error mihai.c@xorte.ch ")

    try:
        thread32 = Thread(target=dellls, args=('mihai.ci@xorte.ch',), daemon=True)

    except:
        print("Error mihai.ci@xorte.ch ")

    try:
        thread33 = Thread(target=dellls, args=('efim.s@xorai.tech',), daemon=True)

    except:
        print("Error efim.s@xorai.tech ")

    try:
        thread34 = Thread(target=dellls, args=('efim.sa@xorai.tech',), daemon=True)

    except:
        print("Error efim.sa@xorai.tech ")

    try:
        thread35 = Thread(target=dellls, args=('efim.s@xorte.ch',), daemon=True)

    except:
        print("Error efim.s@xorte.ch ")

    try:
        thread36 = Thread(target=dellls, args=('efim.sa@xorte.ch',), daemon=True)

    except:
        print("Error efim.sa@xorte.ch ")

    try:
        thread37 = Thread(target=dellls, args=('mihaela.v@xorai.tech',), daemon=True)

    except:
        print("Error mihaela.v@xorai.tech ")

    try:
        thread38 = Thread(target=dellls, args=('mihaela.vi@xorai.tech',), daemon=True)

    except:
        print("Error mihaela.vi@xorai.tech ")

    try:
        thread39 = Thread(target=dellls, args=('mihaela.v@xorte.ch',), daemon=True)

    except:
        print("Error mihaela.v@xorte.ch ")

    try:
        thread40 = Thread(target=dellls, args=('mihaela.vi@xorte.ch',), daemon=True)

    except:
        print("Error mihaela.vi@xorte.ch ")

    try:
        thread41 = Thread(target=dellls, args=('victor.z@xorai.tech',), daemon=True)

    except:
        print("Error victor.z@xorai.tech ")

    try:
        thread42 = Thread(target=dellls, args=('victor.za@xorai.tech',), daemon=True)

    except:
        print("Error victor.za@xorai.tech ")

    try:
        thread43 = Thread(target=dellls, args=('victor.z@xorte.ch',), daemon=True)

    except:
        print("Error victor.z@xorte.ch ")

    try:
        thread44 = Thread(target=dellls, args=('victor.za@xorte.ch',), daemon=True)

    except:
        print("Error victor.za@xorte.ch ")

    try:
        thread45 = Thread(target=dellls, args=('anna.v@xorai.tech',), daemon=True)

    except:
        print("Error anna.v@xorai.tech ")

    try:
        thread46 = Thread(target=dellls, args=('anna.va@xorai.tech',), daemon=True)

    except:
        print("Error anna.va@xorai.tech ")

    try:
        thread47 = Thread(target=dellls, args=('anna.v@xorte.ch',), daemon=True)

    except:
        print("Error anna.v@xorte.ch ")

    try:
        thread48 = Thread(target=dellls, args=('anna.va@xorte.ch',), daemon=True)

    except:
        print("Error anna.va@xorte.ch ")

    try:
        thread49 = Thread(target=dellls, args=('aurel.u@xorai.tech',), daemon=True)

    except:
        print("Error aurel.u@xorai.tech ")

    try:
        thread50 = Thread(target=dellls, args=('aurel.un@xorai.tech',), daemon=True)

    except:
        print("Error aurel.un@xorai.tech ")

    try:
        thread51 = Thread(target=dellls, args=('aurel.u@xorte.ch',), daemon=True)

    except:
        print("Error aurel.u@xorte.ch ")

    try:
        thread52 = Thread(target=dellls, args=('aurel.un@xorte.ch',), daemon=True)

    except:
        print("Error aurel.un@xorte.ch ")

    try:
        thread53 = Thread(target=dellls, args=('vladislav.z@xorai.tech',), daemon=True)

    except:
        print("Error vladislav.z@xorai.tech ")

    try:
        thread54 = Thread(target=dellls, args=('vladislav.za@xorai.tech',), daemon=True)

    except:
        print("Error vladislav.za@xorai.tech ")

    try:
        thread55 = Thread(target=dellls, args=('vladislav.z@xorte.ch',), daemon=True)

    except:
        print("Error vladislav.z@xorte.ch ")

    try:
        thread56 = Thread(target=dellls, args=('vladislav.za@xorte.ch',), daemon=True)

    except:
        print("Error vladislav.za@xorte.ch ")

    try:
        thread57 = Thread(target=dellls, args=('xenia.p@xorai.tech',), daemon=True)

    except:
        print("Error xenia.p@xorai.tech ")

    try:
        thread58 = Thread(target=dellls, args=('xenia.pe@xorai.tech',), daemon=True)

    except:
        print("Error xenia.pe@xorai.tech ")

    try:
        thread59 = Thread(target=dellls, args=('xenia.p@xorte.ch',), daemon=True)

    except:
        print("Error xenia.p@xorte.ch ")

    try:
        thread60 = Thread(target=dellls, args=('xenia.pe@xorte.ch',), daemon=True)

    except:
        print("Error xenia.pe@xorte.ch ")

    try:
        thread61 = Thread(target=dellls, args=('gleb.b@xorai.tech',), daemon=True)

    except:
        print("Error gleb.b@xorai.tech ")

    try:
        thread62 = Thread(target=dellls, args=('gleb.bo@xorai.tech',), daemon=True)

    except:
        print("Error gleb.bo@xorai.tech ")

    try:
        thread63 = Thread(target=dellls, args=('Gleb.b@xorte.ch',), daemon=True)

    except:
        print("Error Gleb.b@xorte.ch ")

    try:
        thread64 = Thread(target=dellls, args=('gleb.bo@xorte.ch',), daemon=True)

    except:
        print("Error gleb.bo@xorte.ch ")

    try:
        thread65 = Thread(target=dellls, args=('rodion.p@xorai.tech',), daemon=True)

    except:
        print("Error rodion.p@xorai.tech ")

    try:
        thread66 = Thread(target=dellls, args=('rodion.pa@xorai.tech',), daemon=True)

    except:
        print("Error rodion.pa@xorai.tech ")

    try:
        thread67 = Thread(target=dellls, args=('rodion.p@xorte.ch',), daemon=True)

    except:
        print("Error rodion.p@xorte.ch ")

    try:
        thread68 = Thread(target=dellls, args=('rodion.pa@xorte.ch',), daemon=True)

    except:
        print("Error rodion.pa@xorte.ch ")

    try:
        thread69 = Thread(target=dellls, args=('vsevolod.g@xorai.tech',), daemon=True)

    except:
        print("Error vsevolod.g@xorai.tech ")

    try:
        thread70 = Thread(target=dellls, args=('vsevolod.gh@xorai.tech',), daemon=True)

    except:
        print("Error vsevolod.gh@xorai.tech ")

    try:
        thread71 = Thread(target=dellls, args=('vsevolod.g@xorte.ch',), daemon=True)

    except:
        print("Error vsevolod.g@xorte.ch ")

    try:
        thread72 = Thread(target=dellls, args=('vsevolod.gh@xorte.ch',), daemon=True)

    except:
        print("Error vsevolod.gh@xorte.ch ")

    try:
        thread73 = Thread(target=dellls, args=('george.o@xorai.tech',), daemon=True)

    except:
        print("Error george.o@xorai.tech ")

    try:
        thread74 = Thread(target=dellls, args=('george.oj@xorai.tech',), daemon=True)

    except:
        print("Error george.oj@xorai.tech ")

    try:
        thread75 = Thread(target=dellls, args=('george.o@xorte.ch',), daemon=True)

    except:
        print("Error george.o@xorte.ch ")

    try:
        thread76 = Thread(target=dellls, args=('george.oj@xorte.ch',), daemon=True)

    except:
        print("Error george.oj@xorte.ch ")

    try:
        thread77 = Thread(target=dellls, args=('nelly.p@xorai.tech',), daemon=True)

    except:
        print("Error nelly.p@xorai.tech ")

    try:
        thread78 = Thread(target=dellls, args=('nelly.pa@xorai.tech',), daemon=True)

    except:
        print("Error nelly.pa@xorai.tech ")

    try:
        thread79 = Thread(target=dellls, args=('nelly.p@xorte.ch',), daemon=True)

    except:
        print("Error nelly.p@xorte.ch ")

    try:
        thread80 = Thread(target=dellls, args=('nelly.pa@xorte.ch',), daemon=True)

    except:
        print("Error nelly.pa@xorte.ch ")

    try:
        thread81 = Thread(target=dellls, args=('dima.n@xorai.tech',), daemon=True)

    except:
        print("Error dima.n@xorai.tech ")

    try:
        thread82 = Thread(target=dellls, args=('dima.na@xorai.tech',), daemon=True)

    except:
        print("Error dima.na@xorai.tech ")

    try:
        thread83 = Thread(target=dellls, args=('dima.n@xorte.ch',), daemon=True)

    except:
        print("Error dima.n@xorte.ch ")

    try:
        thread84 = Thread(target=dellls, args=('dima.na@xorte.ch',), daemon=True)

    except:
        print("Error dima.na@xorte.ch ")

    try:
        thread85 = Thread(target=dellls, args=('dorin.g@xorai.tech',), daemon=True)

    except:
        print("Error dorin.g@xorai.tech ")

    try:
        thread86 = Thread(target=dellls, args=('dorin.go@xorai.tech',), daemon=True)

    except:
        print("Error dorin.go@xorai.tech ")

    try:
        thread87 = Thread(target=dellls, args=('dorin.g@xorte.ch',), daemon=True)

    except:
        print("Error dorin.g@xorte.ch ")

    try:
        thread88 = Thread(target=dellls, args=('dorin.go@xorte.ch',), daemon=True)

    except:
        print("Error dorin.go@xorte.ch ")

    try:
        thread89 = Thread(target=dellls, args=('daniel.c@xorai.tech',), daemon=True)

    except:
        print("Error daniel.c@xorai.tech ")

    try:
        thread90 = Thread(target=dellls, args=('daniel.co@xorai.tech',), daemon=True)

    except:
        print("Error daniel.co@xorai.tech ")

    try:
        thread91 = Thread(target=dellls, args=('daniel.c@xorte.ch',), daemon=True)

    except:
        print("Error daniel.c@xorte.ch ")

    try:
        thread92 = Thread(target=dellls, args=('daniel.co@xorte.ch',), daemon=True)

    except:
        print("Error daniel.co@xorte.ch ")

    try:
        thread93 = Thread(target=dellls, args=('dan.m@xorai.tech',), daemon=True)

    except:
        print("Error dan.m@xorai.tech ")

    try:
        thread94 = Thread(target=dellls, args=('dan.mo@xorai.tech',), daemon=True)

    except:
        print("Error dan.mo@xorai.tech ")

    try:
        thread95 = Thread(target=dellls, args=('dan.m@xorte.ch',), daemon=True)

    except:
        print("Error dan.m@xorte.ch ")

    try:
        thread96 = Thread(target=dellls, args=('dan.mo@xorte.ch',), daemon=True)

    except:
        print("Error dan.mo@xorte.ch ")

    try:
        thread97 = Thread(target=dellls, args=('alevtina.m@xorai.tech',), daemon=True)

    except:
        print("Error alevtina.m@xorai.tech ")

    try:
        thread98 = Thread(target=dellls, args=('alevtina.m@xorte.ch',), daemon=True)

    except:
        print("Error alevtina.m@xorte.ch ")
except:
    print("Error 10 from 10")


try:
    try:
        thread1.start()
    except:
        print("error start  anton.c@xorai.tech")

    try:
        thread2.start()
    except:
        print("error start  anton.ce@xorai.tech")

    try:
        thread3.start()
    except:
        print("error start  anton.c@xorte.ch")

    try:
        thread4.start()
    except:
        print("error start  anton.ce@xorte.ch")

    try:
        thread5.start()
    except:
        print("error start  ernest.s@xorai.tech")

    try:
        thread6.start()
    except:
        print("error start  ernest.sv@xorai.tech")

    try:
        thread7.start()
    except:
        print("error start  ernest.s@xorte.ch")

    try:
        thread8.start()
    except:
        print("error start  ernest.sv@xorte.ch")

    try:
        thread9.start()
    except:
        print("error start  patrisia.g@xorai.tech")

    try:
        thread10.start()
    except:
        print("error start  patrisia.gh@xorai.tech")

    try:
        thread11.start()
    except:
        print("error start  patrisia.g@xorte.ch")

    try:
        thread12.start()
    except:
        print("error start  patrisia.gh@xorte.ch")

    try:
        thread13.start()
    except:
        print("error start  eugen.p@xorai.tech")

    try:
        thread14.start()
    except:
        print("error start  eugen.po@xorai.tech")

    try:
        thread15.start()
    except:
        print("error start  eugen.p@xorte.ch")

    try:
        thread16.start()
    except:
        print("error start  eugen.po@xorte.ch")

    try:
        thread17.start()
    except:
        print("error start  vlad.f@xorai.tech")

    try:
        thread18.start()
    except:
        print("error start  vlad.fo@xorai.tech")

    try:
        thread19.start()
    except:
        print("error start  vlad.f@xorte.ch")

    try:
        thread20.start()
    except:
        print("error start  vlad.fo@xorte.ch")

    try:
        thread21.start()
    except:
        print("error start  victoria.s@xorai.tech")

    try:
        thread22.start()
    except:
        print("error start  victoria.se@xorai.tech")

    try:
        thread23.start()
    except:
        print("error start  victoria.s@xorte.ch")

    try:
        thread24.start()
    except:
        print("error start  victoria.se@xorte.ch")

    try:
        thread25.start()
    except:
        print("error start  dmitrii.c@xorai.tech")

    try:
        thread26.start()
    except:
        print("error start  dmitrii.ca@xorai.tech")

    try:
        thread27.start()
    except:
        print("error start  dmitrii.c@xorte.ch")

    try:
        thread28.start()
    except:
        print("error start  dmitrii.ca@xorte.ch")

    try:
        thread29.start()
    except:
        print("error start  mihai.c@xorai.tech")

    try:
        thread30.start()
    except:
        print("error start  mihai.ci@xorai.tech")

    try:
        thread31.start()
    except:
        print("error start  mihai.c@xorte.ch")

    try:
        thread32.start()
    except:
        print("error start  mihai.ci@xorte.ch")

    try:
        thread33.start()
    except:
        print("error start  efim.s@xorai.tech")

    try:
        thread34.start()
    except:
        print("error start  efim.sa@xorai.tech")

    try:
        thread35.start()
    except:
        print("error start  efim.s@xorte.ch")

    try:
        thread36.start()
    except:
        print("error start  efim.sa@xorte.ch")

    try:
        thread37.start()
    except:
        print("error start  mihaela.v@xorai.tech")

    try:
        thread38.start()
    except:
        print("error start  mihaela.vi@xorai.tech")

    try:
        thread39.start()
    except:
        print("error start  mihaela.v@xorte.ch")

    try:
        thread40.start()
    except:
        print("error start  mihaela.vi@xorte.ch")

    try:
        thread41.start()
    except:
        print("error start  victor.z@xorai.tech")

    try:
        thread42.start()
    except:
        print("error start  victor.za@xorai.tech")

    try:
        thread43.start()
    except:
        print("error start  victor.z@xorte.ch")

    try:
        thread44.start()
    except:
        print("error start  victor.za@xorte.ch")

    try:
        thread45.start()
    except:
        print("error start  anna.v@xorai.tech")

    try:
        thread46.start()
    except:
        print("error start  anna.va@xorai.tech")

    try:
        thread47.start()
    except:
        print("error start  anna.v@xorte.ch")

    try:
        thread48.start()
    except:
        print("error start  anna.va@xorte.ch")

    try:
        thread49.start()
    except:
        print("error start  aurel.u@xorai.tech")

    try:
        thread50.start()
    except:
        print("error start  aurel.un@xorai.tech")

    try:
        thread51.start()
    except:
        print("error start  aurel.u@xorte.ch")

    try:
        thread52.start()
    except:
        print("error start  aurel.un@xorte.ch")

    try:
        thread53.start()
    except:
        print("error start  vladislav.z@xorai.tech")

    try:
        thread54.start()
    except:
        print("error start  vladislav.za@xorai.tech")

    try:
        thread55.start()
    except:
        print("error start  vladislav.z@xorte.ch")

    try:
        thread56.start()
    except:
        print("error start  vladislav.za@xorte.ch")

    try:
        thread57.start()
    except:
        print("error start  xenia.p@xorai.tech")

    try:
        thread58.start()
    except:
        print("error start  xenia.pe@xorai.tech")

    try:
        thread59.start()
    except:
        print("error start  xenia.p@xorte.ch")

    try:
        thread60.start()
    except:
        print("error start  xenia.pe@xorte.ch")

    try:
        thread61.start()
    except:
        print("error start  gleb.b@xorai.tech")

    try:
        thread62.start()
    except:
        print("error start  gleb.bo@xorai.tech")

    try:
        thread63.start()
    except:
        print("error start  Gleb.b@xorte.ch")

    try:
        thread64.start()
    except:
        print("error start  gleb.bo@xorte.ch")

    try:
        thread65.start()
    except:
        print("error start  rodion.p@xorai.tech")

    try:
        thread66.start()
    except:
        print("error start  rodion.pa@xorai.tech")

    try:
        thread67.start()
    except:
        print("error start  rodion.p@xorte.ch")

    try:
        thread68.start()
    except:
        print("error start  rodion.pa@xorte.ch")

    try:
        thread69.start()
    except:
        print("error start  vsevolod.g@xorai.tech")

    try:
        thread70.start()
    except:
        print("error start  vsevolod.gh@xorai.tech")

    try:
        thread71.start()
    except:
        print("error start  vsevolod.g@xorte.ch")

    try:
        thread72.start()
    except:
        print("error start  vsevolod.gh@xorte.ch")

    try:
        thread73.start()
    except:
        print("error start  george.o@xorai.tech")

    try:
        thread74.start()
    except:
        print("error start  george.oj@xorai.tech")

    try:
        thread75.start()
    except:
        print("error start  george.o@xorte.ch")

    try:
        thread76.start()
    except:
        print("error start  george.oj@xorte.ch")

    try:
        thread77.start()
    except:
        print("error start  nelly.p@xorai.tech")

    try:
        thread78.start()
    except:
        print("error start  nelly.pa@xorai.tech")

    try:
        thread79.start()
    except:
        print("error start  nelly.p@xorte.ch")

    try:
        thread80.start()
    except:
        print("error start  nelly.pa@xorte.ch")

    try:
        thread81.start()
    except:
        print("error start  dima.n@xorai.tech")

    try:
        thread82.start()
    except:
        print("error start  dima.na@xorai.tech")

    try:
        thread83.start()
    except:
        print("error start  dima.n@xorte.ch")

    try:
        thread84.start()
    except:
        print("error start  dima.na@xorte.ch")

    try:
        thread85.start()
    except:
        print("error start  dorin.g@xorai.tech")

    try:
        thread86.start()
    except:
        print("error start  dorin.go@xorai.tech")

    try:
        thread87.start()
    except:
        print("error start  dorin.g@xorte.ch")

    try:
        thread88.start()
    except:
        print("error start  dorin.go@xorte.ch")

    try:
        thread89.start()
    except:
        print("error start  daniel.c@xorai.tech")

    try:
        thread90.start()
    except:
        print("error start  daniel.co@xorai.tech")

    try:
        thread91.start()
    except:
        print("error start  daniel.c@xorte.ch")

    try:
        thread92.start()
    except:
        print("error start  daniel.co@xorte.ch")

    try:
        thread93.start()
    except:
        print("error start  dan.m@xorai.tech")

    try:
        thread94.start()
    except:
        print("error start  dan.mo@xorai.tech")

    try:
        thread95.start()
    except:
        print("error start  dan.m@xorte.ch")

    try:
        thread96.start()
    except:
        print("error start  dan.mo@xorte.ch")

    try:
        thread97.start()
    except:
        print("error start  alevtina.m@xorai.tech")

    try:
        thread98.start()
    except:
        print("error start  alevtina.m@xorte.ch")
except:
    print("global error start ")


try:
    try:
        thread1.join()
    except:
        print("error close  anton.c@xorai.tech")

    try:
        thread2.join()
    except:
        print("error close  anton.ce@xorai.tech")

    try:
        thread3.join()
    except:
        print("error close  anton.c@xorte.ch")

    try:
        thread4.join()
    except:
        print("error close  anton.ce@xorte.ch")

    try:
        thread5.join()
    except:
        print("error close  ernest.s@xorai.tech")

    try:
        thread6.join()
    except:
        print("error close  ernest.sv@xorai.tech")

    try:
        thread7.join()
    except:
        print("error close  ernest.s@xorte.ch")

    try:
        thread8.join()
    except:
        print("error close  ernest.sv@xorte.ch")

    try:
        thread9.join()
    except:
        print("error close  patrisia.g@xorai.tech")

    try:
        thread10.join()
    except:
        print("error close  patrisia.gh@xorai.tech")

    try:
        thread11.join()
    except:
        print("error close  patrisia.g@xorte.ch")

    try:
        thread12.join()
    except:
        print("error close  patrisia.gh@xorte.ch")

    try:
        thread13.join()
    except:
        print("error close  eugen.p@xorai.tech")

    try:
        thread14.join()
    except:
        print("error close  eugen.po@xorai.tech")

    try:
        thread15.join()
    except:
        print("error close  eugen.p@xorte.ch")

    try:
        thread16.join()
    except:
        print("error close  eugen.po@xorte.ch")

    try:
        thread17.join()
    except:
        print("error close  vlad.f@xorai.tech")

    try:
        thread18.join()
    except:
        print("error close  vlad.fo@xorai.tech")

    try:
        thread19.join()
    except:
        print("error close  vlad.f@xorte.ch")

    try:
        thread20.join()
    except:
        print("error close  vlad.fo@xorte.ch")

    try:
        thread21.join()
    except:
        print("error close  victoria.s@xorai.tech")

    try:
        thread22.join()
    except:
        print("error close  victoria.se@xorai.tech")

    try:
        thread23.join()
    except:
        print("error close  victoria.s@xorte.ch")

    try:
        thread24.join()
    except:
        print("error close  victoria.se@xorte.ch")

    try:
        thread25.join()
    except:
        print("error close  dmitrii.c@xorai.tech")

    try:
        thread26.join()
    except:
        print("error close  dmitrii.ca@xorai.tech")

    try:
        thread27.join()
    except:
        print("error close  dmitrii.c@xorte.ch")

    try:
        thread28.join()
    except:
        print("error close  dmitrii.ca@xorte.ch")

    try:
        thread29.join()
    except:
        print("error close  mihai.c@xorai.tech")

    try:
        thread30.join()
    except:
        print("error close  mihai.ci@xorai.tech")

    try:
        thread31.join()
    except:
        print("error close  mihai.c@xorte.ch")

    try:
        thread32.join()
    except:
        print("error close  mihai.ci@xorte.ch")

    try:
        thread33.join()
    except:
        print("error close  efim.s@xorai.tech")

    try:
        thread34.join()
    except:
        print("error close  efim.sa@xorai.tech")

    try:
        thread35.join()
    except:
        print("error close  efim.s@xorte.ch")

    try:
        thread36.join()
    except:
        print("error close  efim.sa@xorte.ch")

    try:
        thread37.join()
    except:
        print("error close  mihaela.v@xorai.tech")

    try:
        thread38.join()
    except:
        print("error close  mihaela.vi@xorai.tech")

    try:
        thread39.join()
    except:
        print("error close  mihaela.v@xorte.ch")

    try:
        thread40.join()
    except:
        print("error close  mihaela.vi@xorte.ch")

    try:
        thread41.join()
    except:
        print("error close  victor.z@xorai.tech")

    try:
        thread42.join()
    except:
        print("error close  victor.za@xorai.tech")

    try:
        thread43.join()
    except:
        print("error close  victor.z@xorte.ch")

    try:
        thread44.join()
    except:
        print("error close  victor.za@xorte.ch")

    try:
        thread45.join()
    except:
        print("error close  anna.v@xorai.tech")

    try:
        thread46.join()
    except:
        print("error close  anna.va@xorai.tech")

    try:
        thread47.join()
    except:
        print("error close  anna.v@xorte.ch")

    try:
        thread48.join()
    except:
        print("error close  anna.va@xorte.ch")

    try:
        thread49.join()
    except:
        print("error close  aurel.u@xorai.tech")

    try:
        thread50.join()
    except:
        print("error close  aurel.un@xorai.tech")

    try:
        thread51.join()
    except:
        print("error close  aurel.u@xorte.ch")

    try:
        thread52.join()
    except:
        print("error close  aurel.un@xorte.ch")

    try:
        thread53.join()
    except:
        print("error close  vladislav.z@xorai.tech")

    try:
        thread54.join()
    except:
        print("error close  vladislav.za@xorai.tech")

    try:
        thread55.join()
    except:
        print("error close  vladislav.z@xorte.ch")

    try:
        thread56.join()
    except:
        print("error close  vladislav.za@xorte.ch")

    try:
        thread57.join()
    except:
        print("error close  xenia.p@xorai.tech")

    try:
        thread58.join()
    except:
        print("error close  xenia.pe@xorai.tech")

    try:
        thread59.join()
    except:
        print("error close  xenia.p@xorte.ch")

    try:
        thread60.join()
    except:
        print("error close  xenia.pe@xorte.ch")

    try:
        thread61.join()
    except:
        print("error close  gleb.b@xorai.tech")

    try:
        thread62.join()
    except:
        print("error close  gleb.bo@xorai.tech")

    try:
        thread63.join()
    except:
        print("error close  Gleb.b@xorte.ch")

    try:
        thread64.join()
    except:
        print("error close  gleb.bo@xorte.ch")

    try:
        thread65.join()
    except:
        print("error close  rodion.p@xorai.tech")

    try:
        thread66.join()
    except:
        print("error close  rodion.pa@xorai.tech")

    try:
        thread67.join()
    except:
        print("error close  rodion.p@xorte.ch")

    try:
        thread68.join()
    except:
        print("error close  rodion.pa@xorte.ch")

    try:
        thread69.join()
    except:
        print("error close  vsevolod.g@xorai.tech")

    try:
        thread70.join()
    except:
        print("error close  vsevolod.gh@xorai.tech")

    try:
        thread71.join()
    except:
        print("error close  vsevolod.g@xorte.ch")

    try:
        thread72.join()
    except:
        print("error close  vsevolod.gh@xorte.ch")

    try:
        thread73.join()
    except:
        print("error close  george.o@xorai.tech")

    try:
        thread74.join()
    except:
        print("error close  george.oj@xorai.tech")

    try:
        thread75.join()
    except:
        print("error close  george.o@xorte.ch")

    try:
        thread76.join()
    except:
        print("error close  george.oj@xorte.ch")

    try:
        thread77.join()
    except:
        print("error close  nelly.p@xorai.tech")

    try:
        thread78.join()
    except:
        print("error close  nelly.pa@xorai.tech")

    try:
        thread79.join()
    except:
        print("error close  nelly.p@xorte.ch")

    try:
        thread80.join()
    except:
        print("error close  nelly.pa@xorte.ch")

    try:
        thread81.join()
    except:
        print("error close  dima.n@xorai.tech")

    try:
        thread82.join()
    except:
        print("error close  dima.na@xorai.tech")

    try:
        thread83.join()
    except:
        print("error close  dima.n@xorte.ch")

    try:
        thread84.join()
    except:
        print("error close  dima.na@xorte.ch")

    try:
        thread85.join()
    except:
        print("error close  dorin.g@xorai.tech")

    try:
        thread86.join()
    except:
        print("error close  dorin.go@xorai.tech")

    try:
        thread87.join()
    except:
        print("error close  dorin.g@xorte.ch")

    try:
        thread88.join()
    except:
        print("error close  dorin.go@xorte.ch")

    try:
        thread89.join()
    except:
        print("error close  daniel.c@xorai.tech")

    try:
        thread90.join()
    except:
        print("error close  daniel.co@xorai.tech")

    try:
        thread91.join()
    except:
        print("error close  daniel.c@xorte.ch")

    try:
        thread92.join()
    except:
        print("error close  daniel.co@xorte.ch")

    try:
        thread93.join()
    except:
        print("error close  dan.m@xorai.tech")

    try:
        thread94.join()
    except:
        print("error close  dan.mo@xorai.tech")

    try:
        thread95.join()
    except:
        print("error close  dan.m@xorte.ch")

    try:
        thread96.join()
    except:
        print("error close  dan.mo@xorte.ch")

    try:
        thread97.join()
    except:
        print("error close  alevtina.m@xorai.tech")

    try:
        thread98.join()
    except:
        print("error close  alevtina.m@xorte.ch")
except:
    print('Global error close')



t = str(datetime.datetime.today())
print(t_, t)