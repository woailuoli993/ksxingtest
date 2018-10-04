# -*- coding: utf-8 -*-
from functools import reduce


class OfoPassword(object):
    """
    every sig has four type. total four
    encode 1111 >>> AAAA
    decode 01 01 01 01 >>> 1111
    """
    SIG_1 = '1'
    SIG_2 = '2'
    SIG_3 = '3'
    SIG_4 = '4'
    pass_map = {
        SIG_1: 0,
        SIG_2: 1,
        SIG_3: 2,
        SIG_4: 3
    }

    def __init__(self, password):
        """
        :type password string
        """
        self.password = password

    def _encode(self, sig):
        """sig to pass"""
        return self.pass_map[sig]

    def encode(self):
        keys = reduce(lambda x, y: x << 2 + y, map(self._encode, self.password))

        return keys
