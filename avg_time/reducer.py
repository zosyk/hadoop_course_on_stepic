#!/usr/bin/python

import sys

pairs = {}
for line in sys.stdin:
    (key, value) = line.strip().split("\t")

    pairs[key] = pairs.get(key, []) + [int(value)]

for key, list in pairs.items():
    print(key + "\t" + str(int(sum(list)/len(list))))
