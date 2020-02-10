
# -*- coding: utf-8 -*-

"""
Created on 24.12.19

:author: Bologov V.A.
:email: vasiliybologov@gmail.com

"""




import imaplib


senders = ['anton.c@xorai.tech', 'anton.ce@xorai.tech', 'anton.c@xorte.ch', 'anton.ce@xorte.ch', 'ernest.s@xorai.tech', 'ernest.sv@xorai.tech', 'ernest.s@xorte.ch', 'ernest.sv@xorte.ch', 'patrisia.g@xorai.tech', 'patrisia.gh@xorai.tech', 'patrisia.g@xorte.ch', 'patrisia.gh@xorte.ch', 'eugen.p@xorai.tech', 'eugen.po@xorai.tech', 'eugen.p@xorte.ch', 'eugen.po@xorte.ch', 'vlad.f@xorai.tech', 'vlad.fo@xorai.tech', 'vlad.f@xorte.ch', 'vlad.fo@xorte.ch', 'victoria.s@xorai.tech', 'victoria.se@xorai.tech', 'victoria.s@xorte.ch', 'victoria.se@xorte.ch', 'dmitrii.c@xorai.tech', 'dmitrii.ca@xorai.tech', 'dmitrii.c@xorte.ch', 'dmitrii.ca@xorte.ch', 'mihai.c@xorai.tech', 'mihai.ci@xorai.tech', 'mihai.c@xorte.ch', 'mihai.ci@xorte.ch', 'efim.s@xorai.tech', 'efim.sa@xorai.tech', 'efim.s@xorte.ch', 'efim.sa@xorte.ch', 'mihaela.v@xorai.tech', 'mihaela.vi@xorai.tech', 'mihaela.v@xorte.ch', 'mihaela.vi@xorte.ch', 'victor.z@xorai.tech', 'victor.za@xorai.tech', 'victor.z@xorte.ch', 'victor.za@xorte.ch', 'anna.v@xorai.tech', 'anna.va@xorai.tech', 'anna.v@xorte.ch', 'anna.va@xorte.ch', 'aurel.u@xorai.tech', 'aurel.un@xorai.tech', 'aurel.u@xorte.ch', 'aurel.un@xorte.ch', 'vladislav.z@xorai.tech', 'vladislav.za@xorai.tech', 'vladislav.z@xorte.ch', 'vladislav.za@xorte.ch', 'xenia.p@xorai.tech', 'xenia.pe@xorai.tech', 'xenia.p@xorte.ch', 'xenia.pe@xorte.ch', 'gleb.b@xorai.tech', 'gleb.bo@xorai.tech', 'Gleb.b@xorte.ch', 'gleb.bo@xorte.ch', 'rodion.p@xorai.tech', 'rodion.pa@xorai.tech', 'rodion.p@xorte.ch', 'rodion.pa@xorte.ch', 'vsevolod.g@xorai.tech', 'vsevolod.gh@xorai.tech', 'vsevolod.g@xorte.ch', 'vsevolod.gh@xorte.ch', 'george.o@xorai.tech', 'george.oj@xorai.tech', 'george.o@xorte.ch', 'george.oj@xorte.ch', 'nelly.p@xorai.tech', 'nelly.pa@xorai.tech', 'nelly.p@xorte.ch', 'nelly.pa@xorte.ch', 'dima.n@xorai.tech', 'dima.na@xorai.tech', 'dima.n@xorte.ch', 'dima.na@xorte.ch', 'dorin.g@xorai.tech', 'dorin.go@xorai.tech', 'dorin.g@xorte.ch', 'dorin.go@xorte.ch', 'daniel.c@xorai.tech', 'daniel.co@xorai.tech', 'daniel.c@xorte.ch', 'daniel.co@xorte.ch', 'dan.m@xorai.tech', 'dan.mo@xorai.tech', 'dan.m@xorte.ch', 'dan.mo@xorte.ch', 'alevtina.m@xorai.tech', 'alevtina.m@xorte.ch']

def opens(user, passwd):
    mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    mail.login(user, passwd)
    mail.list()

    mail.select("INBOX", readonly=False)
    result, data = mail.search(None, "ALL")
    ids = data[0]
    id_list = ids.split()
    # print(id_list)

    print(id_list)
    print(str(len(id_list)))
    for mail_id in id_list:
        #print(mail_id)
        no_spam2 = mail.store(mail_id, '+FLAGS', '\Seen')
        no_spam = mail.store(mail_id, '+FLAGS', '\Deleted')
        if no_spam2[0] == 'OK':
            if no_spam[0] == 'OK':
                print("ok1")
            #delete_res = mail.store(mail_id, '+FLAGS', '\Deleted')
        # no_spam = mail.store(mail_id, '+FLAGS', '$NotPhishing')
        """copy_res = mail.copy(mail_id, 'INBOX')
        if copy_res[0] == 'OK':
            print("ok2")
            delete_res = mail.store(mail_id, '+FLAGS', '$NotPhishing')"""


    mail.expunge()


o = 0
while o < len(senders):
    try:
        print("try del mail on " + senders[o])
        opens(senders[o], 'Superxor42')
        o+=1
    except:
        print("----------- error from opens mail on " + senders[o])
        o += 1


print("end del")