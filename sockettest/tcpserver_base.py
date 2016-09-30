# -*- coding:utf-8 -*-
from socket import *
import threading
import json
import time


def tcpadd(tcpclisock, addr):
    print '[+]Accept new connection from %s:%s' % addr
    print ''
    while True:
        buffer = []
        while True:
            print '[~]wating for client say...'
            d = tcpclisock.recv(20)
            print 'get', d
            if len(d) < 20:
                break
        buffer.append(d)
        data = ''.join(buffer)
        print '<<- client say:', data
        data = int(data)
        data += 1
        tcpclisock.send(str(data))
        print '->> server say:', str(data)

host = '0.0.0.0'
port = 13001
addr = (host, port)

tcpsersock = socket(AF_INET, SOCK_STREAM)
tcpsersock.bind(addr)
tcpsersock.listen(5)

# 设置循环是为了接受一个以上的客户端
count = 1
while True:
    print "[~]waiting for client to connect..."
    tcpclisock, addr = tcpsersock.accept()
    print "[+]get conncet from : %s , the %s one" % (addr, count)
    t = threading.Thread(target=tcpadd, args=(tcpclisock, addr))
    t.start()
    time.sleep(2000)




