

# -*- coding: utf-8 -*-


"""
Created on 28.01.19

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
import os
import sys
import feedparser

print()
print()

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

def sendmailrandom(sendername):
    server = '13.78.187.47'
    port = 25
    subj = 'Merry X-Mas and Happy Holidays '
    subj = 'Time for History ' + str(datetime.datetime.today())

    #text = "SpaceX has gained worldwide attention for a series of historic milestones. It is the only private company capable of returning a spacecraft from low Earth orbit, which it first accomplished in 2010. The company made history again in 2012 when its Dragon spacecraft became the first commercial spacecraft to deliver cargo to and from the International Space Station."

    text = random_news()
    text = text + '\n'
    text = textile.textile(text)

    text = text + "<p>If you would like to unsubscribe and stop receiving these emails click  <a href=" + "'mailto:noreply@getxorai.today?subject=Unsubscribe me&body=Helo, Unsubscribe me'" + ">here</a>.</p>"
    text = text + "<p>Request a demo  <a href=" + "'mailto:seth@hrxor.com?subject=Request a demo&body=Helo, Request a demo'" + ">here</a>.</p>"

    file3000 = open(os.getcwd() + '/3000 words', "r")
    words300 = file3000.readlines()
    words300 = [line.rstrip() for line in words300]
    file3000.close()
    rand = random.randint(50, 100)

    rand_text = ''

    w = 0
    while w < rand:
        r = random.randint(0, len(words300) - 1)
        rand_text = rand_text + words300[r] + '  '
        w += 1
    #print(rand)
    #print(rand_text)

    text = text + '<p style="display:none;"> ' + rand_text + ' </p> '

    # unsubscribe

    s = smtplib.SMTP(server, port)

    a = s.ehlo()
    #print(a)

    #a = s.set_debuglevel(1)
    #print(a)

    you = "vasilii.b@xor.ai"
    # you = "vasiliybologov@gmail.com"
    #you = 'seth.d@xor.ai'
    # you = 'papkova.nelly@gmail.com'
    # you = 'seth@luxairtravel.com'
    # you = 'xor_test@yopmail.com'
    # you = "seth@hrxor.com"
    # you = "Sarah.conelli@outlook.com"
    # you = 'Seth_04@xorsurvey.com'
    # you = 'vanessa@flybusinessforless.com'
    # you = 'MoldMD01@gmail.com'




    me = sendername
    dt = datetime.datetime.now()

    t = str(email.utils.format_datetime(dt))
    #print(t)
    mme = me.split(' ')
    meFname = mme[0]
    meLname = mme[1]

    # формирование сообщения
    # msg = MIMEText(text, 'plain', 'cp1251')
    msg = MIMEText(text, 'html', 'utf-8')

    mail_from = meFname + " " + meLname + "  <" + meFname + "@xorhr.com" + ">"

    reply_to = 'vasilii.b@xor.ai'
    # reply_to = 'seth.d@xor.ai'
    msg['Date'] = t
    msg['Subject'] = subj
    msg['FROM'] = mail_from
    msg['TO'] = you
    msg['Reply-To'] = reply_to
    msg['List-Unsubscribe'] = "mailto:noreply@xorhr.com"
    msg['List-Unsubscribe-Post'] = 'List-Unsubscribe=One-Click'
    msg['X-Mailer'] = 'SenderXO'
    # try:
    s.sendmail(mail_from, you, msg.as_string())
    # print(a)
    #print("sent")

    s.quit()

def randomname():


    f1name = open(os.getcwd() + '/first_names.all.txt')

    firstnamebase = f1name.readlines()
    f1name.close()

    f2name = open(os.getcwd() + '/last_names.all.txt')

    lastnamebase = f2name.readlines()
    f2name.close()
    # no '\n'
    firstnamebase = [line.rstrip() for line in firstnamebase]
    lastnamebase = [line.rstrip() for line in lastnamebase]
    # title
    firstnamebase = [line.title() for line in firstnamebase]
    lastnamebase = [line.title() for line in lastnamebase]




    rand_1name = random.randint(0, len(firstnamebase))
    rand_2name = random.randint(0, len(lastnamebase))




    randname = firstnamebase[rand_1name] + " " + lastnamebase[rand_2name]

    return randname


"""sename = randomname()

print(sename)

sendmailrandom(sename)"""
error = 0
x = 0
while x < 100:

    sename = randomname()
    r = random.randint(65, 250)
    sys.stdout.write("\rПисем отправлено {}; Текущщее ожидание  {} сек; Отправитель : {} ; Время {}; Ошибок : {} ".format(x + 1, r, sename, datetime.datetime.now().time(), error))
    #print(sename)

    try:
         sendmailrandom(sename)
    except:
        error += 1

    time.sleep(r)

    x += 1