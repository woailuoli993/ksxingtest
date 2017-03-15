#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by vici on 14/03/2017

from ctypes import *
import os

_file = './libudpquery.so'
_path = os.path.join(*(os.path.split(__file__)[:-1] + (_file,)))
_mod = cdll.LoadLibrary(_path)

#int udpquery(char* url, char* host, char* appid, char* key, char* port, char* version, char* buf, int buf_len);
udpquery = _mod.udpquery
udpquery.argtypes = [c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_int]
udpquery.restype = c_int


if __name__ == '__main__':
    url = "gayhub.com"
    host = "cloud.urlsec.qq.com"
    appid = "123123123"
    key = "sdsd"
    port = "15113"
    version = "1.0"
    retbuf = create_string_buffer(2048)
    retlen = 2048
    foolen = udpquery(url, host, appid, key, port, version, retbuf, retlen)
    print 'ok'
    print retbuf.value
    print foolen

    pass