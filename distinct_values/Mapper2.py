#!/usr/bin/python

class Mapper2:


    def map(self, group):
        print(group + "\t1")


def process():

    import sys

    mapper = Mapper2()
    for line in sys.stdin:
        (value, group) = line.strip().split(",")
        mapper.map(group)


process()
