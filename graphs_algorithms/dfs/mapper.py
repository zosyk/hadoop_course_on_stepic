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

        return min_dist, adj_edges


class Mapper:

    def map(self, line):
        print(line.strip())

        min_dist, adj_edges = Parser.parse(line)
        for edge in adj_edges:
            print(edge + "\t" + str(min_dist + 1).upper() + "\t{}")


def main():
    mapper = Mapper()
    for line in stdin:
        mapper.map(line)


main()
