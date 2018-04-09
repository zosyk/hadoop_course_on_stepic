#!/usr/bin/python

from sys import *

class Dijkstra:

    def __init__(self, lines):
        self.__lines = lines

    def compute(self):
        lines = self.__lines

        (v, e) = lines[:1].pop().strip().split()
        v = int(v)

        vertices = {}
        weights = {}

        for i in range(v):
            vertices[i] = []

        for line in lines[1: len(lines) - 1]:
            (f, t, w) = line.strip().split()
            f = int(f) - 1
            t = int(t) - 1
            w = int(w)

            adj_vertices = vertices.get(f, [])
            adj_vertices.append(t)
            vertices[f] = adj_vertices

            weights[str(f) + " " + str(t)] = w

        (source_vertex, result_vertex) = lines[len(lines) - 1:].pop().split()

        source_vertex = int(source_vertex) - 1
        result_vertex = int(result_vertex) - 1

        d = [None] * v
        q = dict()

        # print(vertices)
        # print(weights)

        for i in range(v):
            d[i] = float("inf")
            q[i] = float("inf")

        d[source_vertex] = 0
        q[source_vertex] = 0

        while q.items():
            min_key = min(q, key=q.get)
            q.pop(min_key)

            for adj_v in vertices.get(min_key):
                calc_weight = d[min_key] + weights.get(str(min_key) + " " + str(adj_v))
                if d[adj_v] > calc_weight:
                    d[adj_v] = calc_weight
                    if q.get(adj_v): q[adj_v] = calc_weight

        for i in range(len(d)):
            if d[i] == float("inf"):
                d[i] = -1

        return d[result_vertex]




def main():
    lines = []
    # for line in stdin:
    #     lines.append(line)
    with open("input/test1.txt") as f:
        lines = f.readlines()

    lines = [x.strip() for x in lines]
    dijkstra = Dijkstra(lines)

    result = dijkstra.compute()

    print(result)



main()
