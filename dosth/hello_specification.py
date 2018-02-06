# -*- coding: utf-8 -*-
from abc import abstractmethod


class Specification(object):

    def and_specification(self, candidate):
        raise NotImplementedError()

    def or_specification(self, candidate):
        raise NotImplementedError()

    def not_specification(self):
        raise NotImplementedError()


class CompositeSpecification(Specification):

    @abstractmethod
    def is_satisfied_by(self, candidate):
        pass

    def and_specification(self, candidate):
        return AndSpecification(self, candidate)

    def or_specification(self, candidate):
        return OrSpecification(self, candidate)

    def not_specification(self):
        return NotSpecification(self)


class AndSpecification(CompositeSpecification):
    _one = Specification()
    _other = Specification()

    def __init__(self, one, other):
        self._one = one
        self._other = other

    def is_satisfied_by(self, candidate):
        return bool(self._one.is_satisfied_by(candidate) and
                    self._other.is_satisfied_by(candidate))


class OrSpecification(CompositeSpecification):
    _one = Specification()
    _other = Specification()

    def __init__(self, one, other):
        self._one = one
        self._other = other

    def is_satisfied_by(self, candidate):
        return bool(self._one.is_satisfied_by(candidate) or
                    self._other.is_satisfied_by(candidate))


class NotSpecification(CompositeSpecification):
    _wrapped = Specification()

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def is_satisfied_by(self, candidate):
        return bool(not self._wrapped.is_satisfied_by(candidate))


class User:

    def __init__(self, archive=True):
        self.archive = archive


class UserSpecification(CompositeSpecification):
    def is_satisfied_by(self, candidate):
        return isinstance(candidate, User)


class UserArciveSpecification(CompositeSpecification):
    def is_satisfied_by(self, candidate):
        return getattr(candidate, 'archive', True)


if __name__ == '__main__':
    print('specification')
    niko = User(archive=True)
    olomeister = User(archive=False)

    the_specification = UserSpecification().\
        and_specification(UserArciveSpecification())

    print(the_specification.is_satisfied_by(niko))
    print(the_specification.is_satisfied_by(olomeister))


