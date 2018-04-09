#!/usr/bin/python

class Mapper:


    def map(self, value, groups):
        for group in groups:
            print(str(value) + "," + group + "\t1")


def process():

    import sys

    mapper = Mapper()
    for line in sys.stdin:
        (value, groupsLine) = line.strip().split("\t")
        groups = groupsLine.split(",")
        mapper.map(value, groups)


process()
