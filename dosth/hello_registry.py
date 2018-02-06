# -*- coding: utf-8 -*-


class RegistryHolder(type):

    REGISTRY = {}

    def __new__(mcs, name, bases, attrs):
        new_cls = type.__new__(mcs, name, bases, attrs)

        mcs.REGISTRY[new_cls.__name__] = new_cls
        return new_cls

    # def __init__(cls, *args, **kwargs):
    #     pass

    @classmethod
    def get_registry(mcs):
        return dict(mcs.REGISTRY)


class ClassRegistree(metaclass=RegistryHolder):
    pass


class ClassregisA(ClassRegistree):
    pass

if __name__ == '__main__':
    print("Before subclassing: ")
    for k in RegistryHolder.get_registry():
        print(k)

    class classregisB(ClassRegistree):
        pass
    print("After subclassing")
    for k in RegistryHolder.get_registry():
        print(k)
