#!/usr/bin/python

import sys


class Reducer:

    def __init__(self):
        self.__values = set()

    def reduce(self, line):
        (value, group) = line.strip().split("\t")
        self.__values.add(value)


    def close(self):
        for value in sorted(self.__values):
            print(value)




def main():
    reducer = Reducer()
    for line in sys.stdin:
        reducer.reduce(line)
    reducer.close()

main()