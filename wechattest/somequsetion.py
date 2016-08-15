#!/usr/bin/python
# _*_ coding:utf-8 _*_

'''神奇的现象'''


def foo(x,l=[]):
    for i in range(x):
        l.append(i**2)
    print l


# f(2)
# f(3, [1, 2, 3])
# f(3)
# f(4)

l = []
#def foo(x,l):
#     def

if __name__=='__main__':
     foo(2)
     foo(3, [1, 2, 3])
     foo(3)

     '''
     辣鸡问题... 详见廖雪峰 python  教程 函数 篇..........
     '''