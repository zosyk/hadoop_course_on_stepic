#!/usr/bin/python

import sys


class Reducer:

    def __init__(self):
        self.__values = dict()

    def reduce(self, line):
        values = self.__values
        (value, group) = line.strip().split("\t")
        values[value] = values.get(value, []) + [value]

    def close(self):
        for key, value in self.__values.items():
            if len(value) == 2:
                print(key)


def main():
    reducer = Reducer()
    for line in sys.stdin:
        reducer.reduce(line)
    reducer.close()


main()
