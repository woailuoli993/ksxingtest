# -*- coding: utf-8 -*-
from unittest.mock import MagicMock, Mock, patch
import unittest


def amimock():
    if func_mock() == 123:
        return 'mock is magic'
    return 'stupid'


def func_mock():
    return 'real.life'
