#!/usr/bin/python

import sys


class Printer:

    def __init__(self, dict):
        self.__dict = dict

    def print1(self):
        for key, value in self.__dict.items():
            print(key + "\t" + str(value))


class Reducer2:

    def __init__(self):
        self.__s = set()
        self.__groups = {}

    def reduce(self, row_line):
        self.__s.add(row_line)

    def close(self):
        groups = self.__groups
        for item in self.__s:
            (value, group) = item.strip().split("\t")
            groups[group] = groups.get(group, 0) + 1

        printer = Printer(groups)
        printer.print1()


def main():
    reducer = Reducer2()
    for line in sys.stdin:
        reducer.reduce(line.strip())

    reducer.close()


main()
