# -*- coding: utf-8 -*-
"""
过年回家网速上行贷款太慢。写个脚本 方便用服务器传书。
唯一需求：传入文件地址， 直接发送文件给 kindle。
"""
import os
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

# config
user = input('email:')
pwd = input('password')
to = ['xxxx@gmail.com']
subject = 'book to you!'
body = 'hello world.'

path = os.path.abspath('')
fp = [os.path.join(path, 'README.rst')]

assert os.path.isfile(fp[0])


def mail(send_from, send_to, subject, text, files=None):
    assert isinstance(send_to, list)

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)

    return msg


if __name__ == '__main__':
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()  # optional
    server.login(user, pwd)

    a_em = mail(user, to, subject, 'a book to you', files=fp)

    server.sendmail(user, to, a_em.as_string())
    server.close()
