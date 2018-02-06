# -*- coding: utf-8 -*-


class A:

    def __init__(self):
        print('a')


class B(A):

    def __init__(self):
        print('b')
        A.__init__(self)  # 这么写不好。


class C(B):

    def __init__(self):
        print("c")
        super().__init__()

A()
print('---------')
B()
print('---------')
C()
