#!/usr/bin/python

from sys import stdin


class Parser:

    @staticmethod
    def parse(line):
        (v, min_dist, adj_edges) = line.strip().split("\t")

        if min_dist.lower() == "inf":
            min_dist = float("inf")
        else:
            min_dist = int(min_dist)

        if len(adj_edges) == 2:
            adj_edges = []
        else:
            adj_edges = adj_edges[1:len(adj_edges) - 1].strip().split(",")

        return v, min_dist, adj_edges


class Reducer:

    def __init__(self):
        self.init_fields(-1, -1, [])

    def reduce(self, line):

        v, min_dist, adj_edges = Parser.parse(line)

        if self.__v == -1:
            self.init_fields(v, min_dist, adj_edges)
        elif self.__v == v:
            self.init_fields(v, min(self.__min_dist, min_dist), max(self.__adj_edges, adj_edges, key=len))
        else:
            self.print_info()
            self.init_fields(v, min_dist, adj_edges)

    def print_info(self):
        print(self.__v + "\t" + str(self.__min_dist).upper() + "\t" + "{" + ",".join(self.__adj_edges) + "}")

    def init_fields(self, v, min_dist, adj_edges):
        self.__v = v
        self.__min_dist = min_dist
        self.__adj_edges = adj_edges


def main():
    reducer = Reducer()
    for line in stdin:
        reducer.reduce(line)
    reducer.print_info()


main()
