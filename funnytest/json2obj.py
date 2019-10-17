# -*- coding: utf-8 -*-

"""convert json  < == > obj
通过 json 实例化. 对象，
编辑之后 再 重新反序列化回 json 是常见操作。
首先是 json 实例化 vm. 类型需要暴露 load 函数，
并且 通过 __init 的 __annotation__ 进行转换.


"""
from collections import OrderedDict
from enum import Enum
from time import sleep

from types import FunctionType

import simplejson as json

UNSET = type('UNSET', (), {'__repr__': lambda self: 'UNSET'})()


def bases(item):
    for base in item.__bases__:
        yield base
        bases(base)


class J2OMeta(type):

    def __new__(mcs, name, bases, namespace):
        fields = OrderedDict()
        types = {}
        for base in bases:
            if issubclass(base, J2OBase) and base != J2OBase:
                fields.update(base.__fields__)
                types.update(getattr(base, '__annotations__', {}))

        annotations = namespace.get('__annotations__', {})
        for key, value in annotations.items():
            if key in namespace:
                fields[key] = namespace[key]
            elif key not in fields:
                fields[key] = UNSET

        new_ns = {
            **{k: v for k, v in namespace.items() if k not in fields},
            '__fields__': fields,
            '__annotations__': {**types, **annotations},
            # '__slots__': set((*types.keys(), *annotations.keys())),
        }
        slots = set([*types.keys(), *annotations.keys()])
        slots.update(['__values__'])
        new_ns.update({'__slots__': slots})
        return type.__new__(mcs, name, bases, new_ns)


class J2OConfig:
    Encoders = {
        Enum: lambda e: e.value,
    }


class J2OBase(metaclass=J2OMeta):

    def __init__(self, *args, **kwargs):
        object.__setattr__(self, '__values__', self.__fields__.copy())
        for key, v in kwargs.items():
            self.__values__[key] = self.__covert_value(key, v)

    def __covert_value(self, key, value):
        aim = self.__annotations__[key]
        if isinstance(aim, list):
            # TODO(yuhua) 序列化的东西。。。
            return [aim[0](**v) for v in value]
        if not isinstance(aim, FunctionType) and isinstance(value, aim):
            return value
        if issubclass(aim, Enum):
            return aim[value]
        if issubclass(aim, J2OBase):
            return aim(**value)

    def __getattr__(self, item):
        try:
            return self.__values__[item]
        except KeyError:
            raise AttributeError(f'"{item}" is not an attribute of '
                                 f'<{self.__class__.__name__}>')

    def __setattr__(self, key, value):
        if key in self.__values__:
            self.__values__[key] = self.__covert_value(key, value)
        else:
            raise ValueError(f'"{key}" is not a field of '
                             f'<{self.__class__.__name__}>')

    @classmethod
    def load(cls, d) -> 'J2OBase':
        """从 dict 或者 json 获取"""
        if isinstance(d, str):
            return json.loads(d, object_hook=cls._json_load_hook)
        elif isinstance(d, dict):
            return cls._from_dict(d)

    @classmethod
    def _from_dict(cls, d: dict) -> 'J2OBase':
        """
        :param d: dict from json load.
        """
        return cls(**d)

    _json_load_hook = _from_dict

    def items(self) -> dict:
        for key, value in self.__values__.items():
            yield key, value

    @classmethod
    def _encode(cls, value):

        if type(value) in J2OConfig.Encoders:
            return J2OConfig.Encoders[type(value)](value)
        elif issubclass(type(value), J2OBase):
            return value.dump()
        elif isinstance(value, (list, set, tuple)):
            return type(value)([cls._encode(v) for v in value])
        for base in bases(type(value)):
            if base in J2OConfig.Encoders:
                return J2OConfig.Encoders[base](value)
        return value

    def dump(self) -> dict:
        return {key: self._encode(v) for key, v in self.items()}


doc_vm = {
    "name": "test_uuid",
    "uuid": "1234",
    "disks": [
        {
            "size": 10086,
            "path": "/usr/lib/python"
    },
        {
            "size": 10000,
            "path": "/usr/lib/golang"
        }
    ],
    "boot": {
        "framework": "uefi",
        "boot_menu": True
    }
}


class Disk(J2OBase):
    size: int
    path: str


class BootFramework(Enum):
    bios = "bios"
    uefi = "uefi"


class Boot(J2OBase):
    framework: BootFramework
    boot_menu: bool


class VM(J2OBase):
    name: str
    uuid: str
    disks: [Disk]
    boot: Boot


if __name__ == '__main__':
    vm = VM.load(doc_vm)

    # print(vm.boot.boot_menu)
    # print(vm.boot.framework)
    # print(vm.disks)
    # for disk in vm.disks:
    #     print(disk.path)
    print(vm.boot.framework)
    print(dict(vm.dump()))
    vm.boot.framework = BootFramework.bios
    print(vm.boot.framework)
    print(dict(vm.dump()))
