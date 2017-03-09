#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by vici on 09/03/2017


def fib():  # 生成器
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


def grep(pattern):
    print "searching for", pattern
    while True:
        line = (yield)
        if pattern in line:
            print line


def coutdown(n):
    print "counting down from", n
    while n > 0:
        newvalue = (yield n)
        if newvalue is not None:
            n = newvalue
        else:
            n -= 1


if __name__ == '__main__':

    # 协程
    # search = grep("coroutine")
    # search.send("Start coroutine! ")
    # search.send("I love you")
    # search.send("Dont you love me")
    # search.send("I love coroutine instead!")
    # 假协程
    c = coutdown(5)
    for n in c:
        print n
        if n == 5:
            c.send(3)