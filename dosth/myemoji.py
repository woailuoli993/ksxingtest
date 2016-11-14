#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by vici on 16-11-14 


def main():
    with open('/home/vici/myem.txt', 'rb') as f:
        myem = f.read()

    print ''.join(map(lambda x: '[em]'+x+'[/em]', set(map(lambda x: x[:4], myem.split(r'[em]')[1:]))))

if __name__ == '__main__':
    main()



# delete emoji that have exist

# like:
# [em]e248[/em][em]e248[/em][em]e251[/em][em]e251[/em][em]e253[/em][em]e253[/em][em]e246[/em][em]e246[/em][em]e245[/em][em]e245[/em][em]e246[/em][em]e245[/em][em]e244[/em][em]e243[/em][em]e251[/em][em]e253[/em][em]e248[/em][em]e248[/em][em]e248[/em][em]e251[/em][em]e251[/em][em]e253[/em][em]e253[/em][em]e246[/em][em]e246[/em][em]e245[/em][em]e245[/em][em]e246[/em][em]e245[/em][em]e244[/em][em]e243[/em][em]e251[/em][em]e253[/em][em]e248[/em] [em]e248[/em][em]e249[/em][em]e245[/em][em]e251[/em][em]e247[/em][em]e246[/em][em]e250[/em][em]e251[/em][em]e252[/em][em]e253[/em][em]e248[/em][em]e248[/em][em]e251[/em][em]e251[/em][em]e253[/em][em]e253[/em][em]e246[/em][em]e246[/em][em]e245[/em][em]e245[/em][em]e246[/em][em]e245[/em][em]e244[/em][em]e243[/em][em]e251[/em][em]e253[/em][em]e248[/em][em]e248[/em][em]e248[/em][em]e251[/em][em]e251[/em][em]e253[/em][em]e253[/em][em]e246[/em][em]e246[/em][em]e245[/em][em]e245[/em][em]e246[/em][em]e245[/em][em]e244[/em][em]e243[/em][em]e251[/em][em]e253[/em][em]e248[/em] [em]e248[/em][em]e249[/em][em]e245[/em][em]e251[/em][em]e247[/em][em]e246[/em][em]e250[/em][em]e251[/em][em]e252[/em][em]e253[/em][em]e248[/em][em]e248[/em][em]e251[/em][em]e251[/em][em]e253[/em][em]e253[/em][em]e246[/em][em]e246[/em][em]e245[/em][em]e245[/em][em]e246[/em][em]e245[/em][em]e244[/em][em]e243[/em][em]e251[/em][em]e253[/em][em]e248[/em][em]e248[/em][em]e248[/em][em]e251[/em][em]e251[/em][em]e253[/em][em]e253[/em][em]e246[/em][em]e246[/em][em]e245[/em][em]e245[/em][em]e246[/em][em]e245[/em][em]e244[/em][em]e243[/em][em]e251[/em][em]e253[/em][em]e248[/em] [em]e248[/em][em]e249[/em][em]e245[/em][em]e251[/em][em]e247[/em][em]e246[/em][em]e250[/em][em]e251[/em][em]e252[/em][em]e253[/em]