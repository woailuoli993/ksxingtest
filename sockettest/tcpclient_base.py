# -*- coding:utf-8 -*-
from socket import *
import time

s = socket(AF_INET, SOCK_STREAM)

s.connect(('192.168.223.74', 13001))
count = 1
print '<<- client say: ', count
s.send(str(count))

while True:
    buffer = []
    while True:
        print '[~]waiting for server say...'
        d = s.recv(4096)
        buffer.append(d)
        if len(d) < 4096:
            break

    data = ''.join(buffer)
    print '->> server say:', data
    data = int(data)
    data += 1
    s.send(str(data))
    print'<<- client say:', data
    time.sleep(1)
    #子子孙孙无穷匮也