#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by vici on 16-11-4 
from decimal import Decimal

class game:

    def __init__(self):
        self.x1 = Decimal(3)
        self.x2 = Decimal(3)
        self.x3 = Decimal(3)
        print("x1:  {0}, x2: {1}, x3: {2}".format(self.x1, self.x2, self.x3))
    def paly(self):
        self.x2, self.x3, self.x1 = self.x1*2/3, self.x1/3 + self.x2, self.x3
        print("x1:  {0}, x2: {1}, x3: {2}".format(self.x1, self.x2, self.x3))


def main():
    mygage = game()
    for i in range(0, 10000):
        mygage.paly()


if __name__ == '__main__':
    main()
