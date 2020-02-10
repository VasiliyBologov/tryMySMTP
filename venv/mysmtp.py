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
import email.utils
import datetime
import random
import feedparser

def random_news():
    NewsFeed = feedparser.parse("https://timesofindia.indiatimes.com/rssfeedstopstories.cms")

    NewsFeed = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml?edition=int")

    lenfeed = len(NewsFeed.entries)
    #print(lenfeed)

    ran = random.randint(0, lenfeed - 1)
    entry = NewsFeed.entries[ran]
    text = "BBC published at : " + entry.published + "that : \n" + entry.summary

    return text

    """print(entry.published)
    print("******")
    print(entry.summary)
    print("------News Link--------")
    print(entry.link)"""

# SMTP-сервер


#server = "104.210.52.21"
#server = "40.112.183.134"


#server = "52.161.27.242"
#server = "13.78.229.217"
#server = '13.78.187.47'
#server = "52.161.27.242"
server = '13.78.137.140'


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

subj = 'Merry X-Mas and Happy Holidays '
subj = 'Test new SMTP test 1 ' + str(datetime.datetime.today())

#text = "Hi , \n I'm reaching out to set up a quick call to discuss how XOR can help you automate your communications to go from “cold candidate outreach” to “interview scheduled” in 5 minutes.\n\nGiven your role, In assume that shortening time-to-hire and increasing hiring efficiency is a priority.\n   XOR is helping employers like McDonald’s, IKEA, and Manpower Group hire faster by automating text messages to announce new job postings, screen candidates,\nand schedule interviews, so your recruiting team is only speaking with qualified candidates.\n\nWe also integrate with 30 different ATS’s and job boards and offer the best support and implementation in the industry.\n\nDo you have time for a quick call to discuss how XOR can help you automate your recruiting communications?\n\n\n\n\n\nWith best regards,\n"


text = random_news()
text = text + '\n'


text = textile.textile(text)
# text = textile.textile(text)

# unsubscribe

text = text + "<p>If you would like to unsubscribe and stop receiving these emails click  <a href="+"'mailto:noreply@getxorai.today?subject=Unsubscribe me&body=Helo, Unsubscribe me'"+">here</a>.</p>"


text = text + "<p>Request a demo  <a href="+"'mailto:seth@hrxor.com?subject=Request a demo&body=Helo, Request a demo'"+">here</a>.</p>"

s = smtplib.SMTP(server, port)

"""#s.connect(server, port)
#print(a)"""

a = s.ehlo()
print(a)
"""#a = s.helo()
#print(a)
a = s.ehlo_or_helo_if_needed()
print(a)

#s.starttls()
print(a)"""


"""a = s.helo(name="104.210.52.21")
print("helo  " + str(a))"""

"""a = s.set_debuglevel(1)
print(a)"""


rand_senders = random.randint(0, 98)
print(senders[rand_senders])
me = senders[rand_senders]


you = "vasilii.b@xor.ai"
#you = "vasiliybologov@gmail.com"
#you = 'seth.d@xor.ai'
#you = 'papkova.nelly@gmail.com'
#you = 'seth@luxairtravel.com'

#you = "test_xor@yopmail.com"
#you = "vanessa@luxairtravel.com"
#you = "seth@flybusinessforless.com"
#you = 'seth@hrxor.com'
youu = ["vasilii.b@xor.ai", "seth@luxairtravel.com", "vanessa@luxairtravel.com", "seth@flybusinessforless.com", "seth.d@xor.ai", "seth@hrxor.com"]


dt = datetime.datetime.now()

t = str(email.utils.format_datetime(dt))
#print(t)
mme = me.split('@')
#mes_id = "<" + str(datetime.datetime.today()) + "@" + mme[1] + ">"
#print(mes_id)



# формирование сообщения
# msg = MIMEText(text, 'plain', 'cp1251')
msg = MIMEText(text, 'html', 'utf-8')
#msg['Message-Id'] = mes_id
msg['Date'] = t
msg['Subject'] = subj
#msg['FROM'] = mme[0] + " <" + me + ">"
msg['FROM'] = mme[0] + " <" + mme[0] + "@xor-ai.info" + ">"
msg['Reply-To'] = me
msg['TO'] = you   #','.join(youu)
msg['List-Unsubscribe'] = "mailto:noreply@getxorai.today"
msg['List-Unsubscribe-Post'] = 'List-Unsubscribe=One-Click'
#try:
a = s.sendmail(mme[0] + "@xorwork.com", you, msg.as_string())
print(a)
print("sent")
#except:
    #print(" -----!!!!  error send ")


# цикл разогрева
"""qwe = 0
while qwe < len(senders):
    print(qwe)


    qwer = 0
    while qwer < len(senders):


        you = senders[qwe]
        to = senders[qwer]
        # формирование сообщения
        # msg = MIMEText(text, 'plain', 'cp1251')
        msg = MIMEText(text, 'html', 'utf-8')
        msg['Subject'] = subj
        msg['FROM'] = me
        msg['TO'] = you
        try:
            s.sendmail(me, you, msg.as_string())
            print("sent")
        except:
            print(" -----!!!!  error send ")


        #print("oh")
        qwer += 1

    qwe += 1"""


s.quit()
