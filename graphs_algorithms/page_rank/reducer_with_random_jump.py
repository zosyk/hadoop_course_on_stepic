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

        return v, float(pr), refs


class Reducer:

    def __init__(self):
        self.init_fields()

    def init_fields(self, v=-1, pr=0.0, refs=[]):
        self.__v = v
        self.__pr = pr
        self.__refs = refs

    def print_info(self):   #PR(x) = a*(1/N) + (1-a)*sum(PR(t)/C(t))
        n = 5
        a = 0.1
        self.__pr = a * 1/5 + (1 - a) * self.__pr
        print(self.__v + "\t" + "{:.3f}".format(self.__pr) + "\t" + "{" + ",".join(self.__refs) + "}")

    def reduce(self, line):
        v, pr, refs = Parser.parse(line)
        self.reduce_parsed_values(v, pr, refs)

    def reduce_parsed_values(self, v, pr, refs):
        if self.__v == -1 and len(refs) > 0:
            self.init_fields(v, refs=refs)
        elif self.__v == -1:
            self.init_fields(v, pr=pr)
        elif self.__v == v and len(refs) > 0:
            self.__refs = refs
        elif self.__v == v:
            self.__pr = self.__pr + pr
        else:
            self.print_info()
            self.init_fields(-1)
            self.reduce_parsed_values(v, pr, refs)


def main():
    reducer = Reducer()
    for line in stdin:
        reducer.reduce(line)
    reducer.print_info()


main()
