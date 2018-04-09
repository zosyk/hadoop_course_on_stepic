#!/usr/bin/python

import sys


class Reducer:

    def reduce(self, group):
        print(group)



def main():
    reducer = Reducer()
    groups = set()
    for line in sys.stdin:
        (value, one) = line.strip().split("\t")
        groups.add(value)

    for group in sorted(groups):
        reducer.reduce(group)


main()