#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by vici on 16-10-25 


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def __reversed__(self):
        """反向迭代

        调用反向迭代需要使用reversed()
        """
        pass

    def depth_first(self):
        yield self
        for c in self:
            # this must over python 3.3
            yield from c.depth_first()

    def width_first(self):
        for c in self:
            yield from c.width_first()
        yield self


class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reverse iterator
    def __reversed__(self):
        n  = 1
        while n <= self.start:
            yield n
            n += 1


def main():
    # root = Node(0)
    # child1 = Node(1)
    # child2 = Node(2)
    # root.add_child(child1)
    # root.add_child(child2)
    # child1.add_child(Node(3))
    # child1.add_child(Node(4))
    # child2.add_child(Node(5))
    # # output  root
    # for ch in root.depth_first():
    #     print(ch)
    #
    # print('width first')
    # for ch in root.width_first():
    #     print(ch)
    for ite in Countdown(30):
        print(ite)

    print('reverse')
    for rev in reversed(Countdown(30)):
        print(rev)


if __name__ == '__main__':
    main()
