# -*- coding:utf-8 -*-
import re

__doc__ == """Python 正则测试"""


def a_main():
    line = 'asdf fjdk; afed, fjek,asdf, foo， 花花到此一游  谁敢拦我！'
    print(re.split(r'[;,，\s]\s*', line))


def b_main(m):
    """

    :param m:  经过datepat 匹配到的模式串
    :return: 将匹配串进行内部处理 并返回
    """
    from calendar import month_abbr
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(3), mon_name, m.group(2))

if __name__ == '__main__':
    # a_main()
    text = 'Today is 11/25/2016. PyCon starts 10/15/2016.'
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

    print(datepat.sub(b_main, text))
