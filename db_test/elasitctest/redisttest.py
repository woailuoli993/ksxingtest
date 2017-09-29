#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by vici on 16-11-2 
import redis

myredis = redis.StrictRedis()


def main():
    gg = myredis.get("tesas")
    print gg
    if gg is None:
        print "gg is None"
    pass


if __name__ == '__main__':
    main()
