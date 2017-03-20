#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by vici on 17/03/2017



if __name__ == '__main__':
    with open('testurl.txt', mode='r') as f:
        for line in f:
            print(line.split("?")[0].split("//")[-1].split("/")[0].split(":")[0])
            print('--------------------------------------------------------')
    pass