#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by vici on 09/03/2017
#  python tail -f | understand coroutines

import time


# coroutine decorator
def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        cr.next()
        return cr
    return start


def follow(thefile, target):
    print "start tail"
    thefile.seek(0, 2)
    # seek(x, y ) the default is 0, means file beginning, 1 => current position, 2=> end of file
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        print("[+] get 1 new line")
        target.send(line)


@coroutine
def printer():
    while True:
        line = (yield)
        print line,


if __name__ == '__main__':
    import platform
    print platform.python_version()
    f = open("1", 'rb')
    printt = printer()
    follow(f, printt)



