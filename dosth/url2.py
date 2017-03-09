#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by vici on 08/03/2017
import requests
import time

if __name__ == '__main__':
    with open("new.txt", "ab+") as myfile:
        with open('url.txt', 'r') as f:
            for line in f:

                r = requests.get('http://192.168.223.63/query?url={}'.format(line), timeout=1)

                print r.content

                myfile.write(r.content)

        pass