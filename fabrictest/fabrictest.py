#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by vici on 16-10-27 
from fabric.api import *
from shellrun import shellrun


def deploy():
    local("cal")

if __name__ == '__main__':
    local("fab ")
