# -*- coding: utf-8 -*-
"""
递归获取 组内权限。
"""


class Group(object):
    def __init__(self, pe, groups=None):
        self.pe = pe
        self.groups = groups or []

    @property
    def all_pe(self):
        print('name {}'.format(self.pe))
        if not self.groups:
            return {self.pe}
        else:
            others = reduce(set.union,
                            map(lambda x: getattr(x, 'all_pe'), self.groups))
            others.add(self.pe)
            return others


if __name__ == '__main__':
    a = Group('a')
    b = Group('b')
    c = Group('c')
    d = Group('d')
    e = Group('e', [a, b])
    f = Group('f', [c, d])
    g = Group('g')
    h = Group('h')
    i = Group('i', [e, f])
    j = Group('j', [g, h])
    k = Group('k', [a, b, i, j])
    print(k.all_pe)
    # print(e.all_pe)
    # print(i.all_pe)
