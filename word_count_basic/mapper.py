#! /usr/bin/python
import sys

#cat testText.txt | ./mapper.py | sort | ./reducer.py

for line in sys.stdin:
    for token in line.strip().split(" "):
        if token:
            print("{}\t1".format(token))
