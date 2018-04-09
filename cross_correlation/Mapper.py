#!/usr/bin/python
import sys


class Printer:

    def do_print(self, a, b):
        print("{},{}\t1".format(a, b))


class Mapper:

    def __init__(self):
        self.__printer = Printer()

    def map(self, line):
        array = line.strip().split()

        for i in array:
            for j in array:
                if i == j:
                    continue
                self.__printer.do_print(i, j)


def main():
    mapper = Mapper()

    for line in sys.stdin:
        mapper.map(line)


main()
