# -*- coding: utf-8 -*-
from abc import abstractmethod


class ComputerPart:

    @abstractmethod
    def accept(self, computer_part_visitor):
        pass


class Monitor(ComputerPart):

    def accept(self, computer_part_visitor):
        computer_part_visitor.visit(self)


class KeyBoard(ComputerPart):

    def accept(self, computer_part_visitor):
        computer_part_visitor.visit(self)


class Mouse(ComputerPart):

    def accept(self, computer_part_visitor):
        computer_part_visitor.visit(self)


class Computer(ComputerPart):

    def __init__(self):

        self.parts = [Monitor(), KeyBoard(), Mouse()]

    def accept(self, computer_part_visitor):
        for part in self.parts:
            part.accept(computer_part_visitor)

        computer_part_visitor.visit(self)


class ComputerPartVisitor:

    @abstractmethod
    def visit(self, computer_visitor):
        pass


class ComputerPartDisplayVisitor(ComputerPartVisitor):

    def visit(self, computer_part):
        print("Display " + computer_part.__class__.__name__)


if __name__ == '__main__':
    computer = Computer()
    computer.accept(ComputerPartDisplayVisitor())
