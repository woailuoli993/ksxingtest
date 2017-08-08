#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by vici on 08/08/2017
# request: python version >= 3.4
from functools import partialmethod, partial


class TestPartical(object):

    def __init__(self):
        pass

    def add_two(self, a, b):
        return a + b

    def add_one(self, b):
        _add_one = partial(self.add_two, 1)
        return _add_one(b)

    add_one_2 = partialmethod(add_two, 2)
