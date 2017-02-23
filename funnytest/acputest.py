#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by vici on 15/02/2017
from dosth.testthread import timeit

@timeit
def cputest():
    su = 0
    for i in range(1, 40001):
        for j in range(1, 40001):
            su += i * j
    print(su)
if __name__ == '__main__':

    cputest()

