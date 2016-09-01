# _*_ coding:utf-8 _*_
# using python 3
"""
    excel 中 列标志为 A-Z AA-ZZ
    将A -> 1
      AA -> 27
"""
import string

alpTomun = dict(zip(string.ascii_lowercase, range(1, 27)))
# print(alpTomun)


def getNum(ascStr):

    ascStr = str(ascStr).lower()
    strlen = len(ascStr)
    mysum = 0

    for i in ascStr:

        strlen -= 1
        mysum += alpTomun[i] * 26 ** strlen

    return mysum