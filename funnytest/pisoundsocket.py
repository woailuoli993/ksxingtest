#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by vici on 27/02/2017
import paramiko
import time


ip = '122.138.168.136'

port = 8022
username = 'pi'
password = 'wy'
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip, port,username, password)
cmd='nc -l 8077 > /dev/tty1'#pts/0'
stdin, stdout, stderr = ssh.exec_command(cmd)
#stdin.write('sudo -S %s\n' % password)
#stdin.flush()
out = stdout.readlines()
ssh.close()

if __name__ == '__main__':
    pass