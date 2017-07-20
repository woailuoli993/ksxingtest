#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by vici on 20/07/2017


class ClassProperty:

    def __init__(self, f):
        self.f = f  # where class.method input
        print("init")
        pass

    def __get__(self, instance, owner):
        print("get")
        return self.f(owner)

    def __set__(self, instance, value):
        print("set")


class MyTestClass:
    i = 0

    def __init__(self):
        pass

    @ClassProperty
    def my_i(self):
        self.i = 6
        return self.i


if __name__ == '__main__':

    print(MyTestClass.my_i)
    print(MyTestClass.i)
    pass
