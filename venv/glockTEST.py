# -*- coding: utf-8 -*-


"""
Created on 24.12.19

:
author: Bologov V.A.
:
email: vasiliybologov@gmail.com

"""

import smtplib
from email.mime.text import MIMEText

import textile

import imaplib

import email
import time
import random
import datetime
import email.utils

# SMTP-сервер


server = "104.210.52.21"

port = 25

# user_name = "artur.b@xor.ai"


senders = ['anton.c@xorai.tech', 'anton.ce@xorai.tech', 'anton.c@xorte.ch', 'anton.ce@xorte.ch',
           'ernest.s@xorai.tech', 'ernest.sv@xorai.tech', 'ernest.s@xorte.ch', 'ernest.sv@xorte.ch',
           'patrisia.g@xorai.tech', 'patrisia.gh@xorai.tech', 'patrisia.g@xorte.ch', 'patrisia.gh@xorte.ch',
           'eugen.p@xorai.tech', 'eugen.po@xorai.tech', 'eugen.p@xorte.ch', 'eugen.po@xorte.ch', 'vlad.f@xorai.tech',
           'vlad.fo@xorai.tech', 'vlad.f@xorte.ch', 'vlad.fo@xorte.ch', 'victoria.s@xorai.tech',
           'victoria.se@xorai.tech', 'victoria.s@xorte.ch', 'victoria.se@xorte.ch', 'dmitrii.c@xorai.tech',
           'dmitrii.ca@xorai.tech', 'dmitrii.c@xorte.ch', 'dmitrii.ca@xorte.ch', 'mihai.c@xorai.tech',
           'mihai.ci@xorai.tech', 'mihai.c@xorte.ch', 'mihai.ci@xorte.ch', 'efim.s@xorai.tech', 'efim.sa@xorai.tech',
           'efim.s@xorte.ch', 'efim.sa@xorte.ch', 'mihaela.v@xorai.tech', 'mihaela.vi@xorai.tech', 'mihaela.v@xorte.ch',
           'mihaela.vi@xorte.ch', 'victor.z@xorai.tech', 'victor.za@xorai.tech', 'victor.z@xorte.ch',
           'victor.za@xorte.ch', 'anna.v@xorai.tech', 'anna.va@xorai.tech', 'anna.v@xorte.ch', 'anna.va@xorte.ch',
           'aurel.u@xorai.tech', 'aurel.un@xorai.tech', 'aurel.u@xorte.ch', 'aurel.un@xorte.ch',
           'vladislav.z@xorai.tech', 'vladislav.za@xorai.tech', 'vladislav.z@xorte.ch', 'vladislav.za@xorte.ch',
           'xenia.p@xorai.tech', 'xenia.pe@xorai.tech', 'xenia.p@xorte.ch', 'xenia.pe@xorte.ch', 'gleb.b@xorai.tech',
           'gleb.bo@xorai.tech', 'Gleb.b@xorte.ch', 'gleb.bo@xorte.ch', 'rodion.p@xorai.tech', 'rodion.pa@xorai.tech',
           'rodion.p@xorte.ch', 'rodion.pa@xorte.ch', 'vsevolod.g@xorai.tech', 'vsevolod.gh@xorai.tech',
           'vsevolod.g@xorte.ch', 'vsevolod.gh@xorte.ch', 'george.o@xorai.tech', 'george.oj@xorai.tech',
           'george.o@xorte.ch', 'george.oj@xorte.ch', 'nelly.p@xorai.tech', 'nelly.pa@xorai.tech', 'nelly.p@xorte.ch',
           'nelly.pa@xorte.ch', 'dima.n@xorai.tech', 'dima.na@xorai.tech', 'dima.n@xorte.ch', 'dima.na@xorte.ch',
           'dorin.g@xorai.tech', 'dorin.go@xorai.tech', 'dorin.g@xorte.ch', 'dorin.go@xorte.ch', 'daniel.c@xorai.tech',
           'daniel.co@xorai.tech', 'daniel.c@xorte.ch', 'daniel.co@xorte.ch', 'dan.m@xorai.tech', 'dan.mo@xorai.tech',
           'dan.m@xorte.ch', 'dan.mo@xorte.ch', 'alevtina.m@xorai.tech', 'alevtina.m@xorte.ch']

subj = 'Merry X-Mas and Happy Holidays MySMTP Glosk test'

keytest = "id:2020-01-10-22:08:54:780t"

text = "Hi , \n I'm reaching out to set up a quick call to discuss how XOR can help you automate your communications to go from “cold candidate outreach” to “interview scheduled” in 5 minutes.\n" + keytest + "\nGiven your role, In assume that shortening time-to-hire and increasing hiring efficiency is a priority.\n   XOR is helping employers like McDonald’s, IKEA, and Manpower Group hire faster by automating text messages to announce new job postings, screen candidates,\nand schedule interviews, so your recruiting team is only speaking with qualified candidates.\n\nWe also integrate with 30 different ATS’s and job boards and offer the best support and implementation in the industry.\n\nDo you have time for a quick call to discuss how XOR can help you automate your recruiting communications?\n\n\n\n\n\nWith best regards,\n"

text = textile.textile(text)
# text = textile.textile(text)


text = textile.textile(text)
# text = textile.textile(text)

# unsubscribe

text = text + "<p>If you would like to unsubscribe and stop receiving these emails click  <a href="+"https://xor.ai"+">here:</a>.</p>"

s = smtplib.SMTP(server, port)

# s.ehlo()
#s.helo()
#s.ehlo_or_helo_if_needed()

#s.starttls()

#me = senders[21]
#you = ['ipm13ho@glockapps.com', 'allanb@glockapps.awsapps.com', 'markb@glockapps.awsapps.com', 'ingridmejiasri@aol.com', 'franprohaska@aol.com', 'garrettjacqueline@aol.com', 'leannamccoybr@aol.com', 'julia_g_76@icloud.com', 'gappsglock@icloud.com', 'bcc@spamcombat.com', 'chazb@userflowhq.com', 'janefergusone@gmail.com', 'louiepettydr@gmail.com', 'lenorebayerd@gmail.com', 'cierawilliamsonwq@gmail.com', 'silviacopelandqy@gmail.com', 'daishacorwingx@gmail.com', 'verify79@buyemailsoftware.com', 'joanyedonald@gmail.com', 'emilikerr@gmail.com', 'wandammorrison@gmail.com', 'lawrenceleddylr@gmail.com', 'alisonnlawrence@gmail.com', 'tinamallahancr@gmail.com', 'verifycom79@gmx.com', 'gd@desktopemail.com', 'jpatton@fastdirectorysubmitter.com', 'frankiebeckerp@hotmail.com', 'b2bdeliver79@mail.com', 'glockapps@mc.glockapps.com', 'nsallan@expertarticles.com', 'exosf@glockeasymail.com', 'brendonosbornx@outlook.com', 'christopherfranklinhk@outlook.com', 'kaceybentleyerp@outlook.com', 'meaghanwittevx@outlook.com', 'aileenjamesua@outlook.com', 'shannongreerf@outlook.com', 'gabrielharberh@outlook.com', 'candidobashirian@outlook.com', 'vincenzaeffertz@outlook.com', 'sa79@justlan.com', 'verifyca79@yahoo.ca', 'justynbenton@yahoo.com', 'emailtester493@yahoo.com', 'loganbridgesrk@yahoo.com', 'rogertoddw@yahoo.com', 'darianhuffg@yahoo.com', 'verifynewssl@zoho.com', 'lamb@glockdb.com']
#you = ['ipm25tf@glockapps.com', 'allanb@glockapps.awsapps.com', 'markb@glockapps.awsapps.com', 'ingridmejiasri@aol.com', 'franprohaska@aol.com', 'garrettjacqueline@aol.com', 'leannamccoybr@aol.com', 'julia_g_76@icloud.com', 'gappsglock@icloud.com', 'bcc@spamcombat.com', 'chazb@userflowhq.com', 'stevebarrydr@fastmail.com', 'verify79@buyemailsoftware.com', 'janefergusone@gmail.com', 'joanyedonald@gmail.com', 'emilikerr@gmail.com', 'wandammorrison@gmail.com', 'lawrenceleddylr@gmail.com', 'alisonnlawrence@gmail.com', 'tinamallahancr@gmail.com', 'louiepettydr@gmail.com', 'lenorebayerd@gmail.com', 'cierawilliamsonwq@gmail.com', 'silviacopelandqy@gmail.com', 'daishacorwingx@gmail.com', 'verifycom79@gmx.com', 'gd@desktopemail.com', 'jpatton@fastdirectorysubmitter.com', 'frankiebeckerp@hotmail.com', 'b2bdeliver79@mail.com', 'glockapps@mc.glockapps.com', 'nsallan@expertarticles.com', 'exosf@glockeasymail.com', 'brendonosbornx@outlook.com', 'christopherfranklinhk@outlook.com', 'kaceybentleyerp@outlook.com', 'meaghanwittevx@outlook.com', 'aileenjamesua@outlook.com', 'shannongreerf@outlook.com', 'gabrielharberh@outlook.com', 'candidobashirian@outlook.com', 'vincenzaeffertz@outlook.com', 'sa79@justlan.com', 'justynbenton@yahoo.com', 'emailtester493@yahoo.com', 'loganbridgesrk@yahoo.com', 'rogertoddw@yahoo.com', 'darianhuffg@yahoo.com', 'verifynewssl@zoho.com', 'lamb@glockdb.com']
#you = ['ipm25yc@glockapps.com', 'allanb@glockapps.awsapps.com', 'markb@glockapps.awsapps.com', 'ingridmejiasri@aol.com', 'franprohaska@aol.com', 'garrettjacqueline@aol.com', 'leannamccoybr@aol.com', 'julia_g_76@icloud.com', 'gappsglock@icloud.com', 'bcc@spamcombat.com', 'chazb@userflowhq.com', 'stevebarrydr@fastmail.com', 'verify79@buyemailsoftware.com', 'janefergusone@gmail.com', 'joanyedonald@gmail.com', 'emilikerr@gmail.com', 'wandammorrison@gmail.com', 'lawrenceleddylr@gmail.com', 'alisonnlawrence@gmail.com', 'tinamallahancr@gmail.com', 'louiepettydr@gmail.com', 'lenorebayerd@gmail.com', 'cierawilliamsonwq@gmail.com', 'silviacopelandqy@gmail.com', 'daishacorwingx@gmail.com', 'verifycom79@gmx.com', 'gd@desktopemail.com', 'jpatton@fastdirectorysubmitter.com', 'frankiebeckerp@hotmail.com', 'b2bdeliver79@mail.com', 'glockapps@mc.glockapps.com', 'nsallan@expertarticles.com', 'exosf@glockeasymail.com', 'brendonosbornx@outlook.com', 'christopherfranklinhk@outlook.com', 'kaceybentleyerp@outlook.com', 'meaghanwittevx@outlook.com', 'aileenjamesua@outlook.com', 'shannongreerf@outlook.com', 'gabrielharberh@outlook.com', 'candidobashirian@outlook.com', 'vincenzaeffertz@outlook.com', 'sa79@justlan.com', 'justynbenton@yahoo.com', 'emailtester493@yahoo.com', 'loganbridgesrk@yahoo.com', 'rogertoddw@yahoo.com', 'darianhuffg@yahoo.com', 'verifynewssl@zoho.com', 'lamb@glockdb.com']
you = ['ipm25yc@glockapps.com', 'allanb@glockapps.awsapps.com', 'markb@glockapps.awsapps.com', 'ingridmejiasri@aol.com', 'franprohaska@aol.com', 'garrettjacqueline@aol.com', 'leannamccoybr@aol.com', 'julia_g_76@icloud.com', 'gappsglock@icloud.com', 'bcc@spamcombat.com', 'chazb@userflowhq.com', 'stevebarrydr@fastmail.com', 'verify79@buyemailsoftware.com', 'janefergusone@gmail.com', 'joanyedonald@gmail.com', 'emilikerr@gmail.com', 'wandammorrison@gmail.com', 'lawrenceleddylr@gmail.com', 'alisonnlawrence@gmail.com', 'tinamallahancr@gmail.com', 'louiepettydr@gmail.com', 'lenorebayerd@gmail.com', 'cierawilliamsonwq@gmail.com', 'silviacopelandqy@gmail.com', 'daishacorwingx@gmail.com', 'verifycom79@gmx.com', 'gd@desktopemail.com', 'jpatton@fastdirectorysubmitter.com', 'frankiebeckerp@hotmail.com', 'b2bdeliver79@mail.com', 'glockapps@mc.glockapps.com', 'nsallan@expertarticles.com', 'exosf@glockeasymail.com', 'brendonosbornx@outlook.com', 'christopherfranklinhk@outlook.com', 'kaceybentleyerp@outlook.com', 'meaghanwittevx@outlook.com', 'aileenjamesua@outlook.com', 'shannongreerf@outlook.com', 'gabrielharberh@outlook.com', 'candidobashirian@outlook.com', 'vincenzaeffertz@outlook.com', 'sa79@justlan.com', 'verifyca79@yahoo.ca', 'justynbenton@yahoo.com', 'emailtester493@yahoo.com', 'loganbridgesrk@yahoo.com', 'rogertoddw@yahoo.com', 'darianhuffg@yahoo.com', 'verifynewssl@zoho.com', 'lamb@glockdb.com']


#you = "vasilii.b@xor.ai"
#you = "mihaela.v@xorte.ch"
#you = 'seth.d@xor.ai'



"""#s.connect(server, port)
#print(a)

#a = s.ehlo()
#print(a)
#a = s.helo()
#print(a)
#a = s.ehlo_or_helo_if_needed()
#print(a)

#s.starttls()
#print(a)"""
rand_senders = random.randint(0, 98)
print(senders[rand_senders])
me = senders[rand_senders]

s = smtplib.SMTP(server, port)



dt = datetime.datetime.now()

t = str(email.utils.format_datetime(dt))
mme = me.split('@')
mes_id = "<" + str(datetime.datetime.today()) + "@" + mme[1] + ">"

# формирование сообщения
# msg = MIMEText(text, 'plain', 'cp1251')
msg = MIMEText(text, 'html', 'utf-8')
#msg['Message-Id'] = mes_id
msg['Date'] = t
msg['Subject'] = subj
msg['FROM'] = mme[0] + " <" + me + ">"
msg['TO'] = ','.join(you)
msg['List-Unsubscribe'] = "mailto:vasilii.b@xor.ai"
msg['List-Unsubscribe-Post'] = 'List-Unsubscribe=One-Click'
#msg['X-Gm-Spam'] = "0"
try:
    s.sendmail(me, you, msg.as_string())
    #print(a)
    print("sent")
except:
    print(" -----!!!!  error send ")



s.quit()