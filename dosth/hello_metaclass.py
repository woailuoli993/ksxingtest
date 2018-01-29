# -*- coding: utf-8 -*-
from abc import ABC, ABCMeta, abstractmethod


class MyIterable(ABC):

    @abstractmethod
    def __iter__(self):
        while False:
            yield None

    def get_iterator(self):
        return self.__iter__()


class MyIterable2(metaclass=ABCMeta):

    @abstractmethod
    def __iter__(self):
        while False:
            yield None
        # ...

    def get_iterator(self):
        return self.__iter__()


@MyIterable.register
class Iter1:
    def __getitem__(self, index):
        ...

    def __len__(self):
        ...

    def get_iterator(self):
        return iter(self)


# 等效
class Iter2(MyIterable2):
    def __getitem__(self, index):
        ...

    def __len__(self):
        ...

    def get_iterator(self):
        return iter(self)

iter1 = Iter1()
print(iter1.__dict__)

print(issubclass(Iter1, MyIterable))  # True
print(isinstance(Iter1, MyIterable))  # False
print(issubclass(Iter2, MyIterable2))  # True
print(isinstance(Iter2, MyIterable2))  # False

# for i in Iter1():
#     print(i)

