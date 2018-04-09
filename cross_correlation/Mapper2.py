#!/usr/bin/python
import sys


class Printer:

    def do_print(self, a, aDict):
        output = "{}\t".format(a)

        for key, value in aDict.items():
            output += "{}:{},".format(key, value)
        print(output[:len(output)-1])


class Mapper:

    def __init__(self):
        self.__printer = Printer()

    def map(self, line):
        array = line.strip().split()
        for i in array:
            iDict = {}
            for j in array:
                if i == j:
                    continue
                iDict[j] = iDict.get(j, 0) + 1
            self.__printer.do_print(i, iDict)
            # print(i + " dict: " + str(iDict))


def main():
    mapper = Mapper()

    for line in sys.stdin:
        mapper.map(line)


main()
