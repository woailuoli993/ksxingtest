# -*- coding: utf-8 -*-
import unittest
import dosth.mocktest


class TestMock(unittest.TestCase):

    def test_func_mock(self, *args):
        print('='*123)
        print("args: {}".format(args))
        dosth.mocktest.func_mock = lambda: 123
        assert dosth.mocktest.amimock() == 'mock is magic'

