#! /usr/bin/python

import sys

(last_key, sum) = (None, 0)

for line in sys.stdin:
    (key, value) = line.strip().split("\t")
    if last_key and last_key != key:
        print("{}\t{}".format(last_key, str(sum)))
        (last_key, sum) = (key, int(value))
    else:
        (last_key, sum) = (key, sum + int(value))

if last_key:
    print("{}\t{}".format(last_key, str(sum)))