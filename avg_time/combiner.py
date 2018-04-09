#!/usr/bin/python

import sys

pairs = {}
for line in sys.stdin:
    (key, value) = line.strip().split("\t")

    (seconds, one) = value.strip().split(";")

    list = pairs.get(key, [0,0])
    list[0] = list[0] + int(seconds)
    list[1] = list[1] + int(one)
    pairs[key] = list

for key, list in pairs.items():
    print(key + "\t" + str(list[0]) + ";" + str(list[1]))
