# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class Pet(metaclass=ABCMeta):

    @classmethod
    def from_name(cls, name):
        for sub_cls in cls.__subclasses__():
            if name == sub_cls.__name__.lower():
                return sub_cls()

    @abstractmethod
    def speak(self):
        """"""


class Kitty(Pet):
    def speak(self):
        return "Miao"


class Duck(Pet):
    def speak(self):
        return "Quak"


for name in ['kitty', 'duck']:
    pet = Pet.from_name(name)
    print("{}: {}".format(name, pet.speak()))
