#!/usr/bin/python

from sys import stdin


class Parser:

    @staticmethod
    def parse(line):
        v, pr, refs = line.strip().split("\t")

        if len(refs) == 2:
            refs = []
        else:
            refs = refs[1:len(refs) - 1].strip().split(",")

        return v, pr, refs


class Mapper:

    def map(self, line):
        print(line.strip())

        v, pr, refs = Parser.parse(line)
        for ref in refs:
            print(ref + "\t" + "{:.3f}".format(float(pr)/len(refs)) + "\t{}")


def main():
    mapper = Mapper()
    for line in stdin:
        mapper.map(line)


main()
