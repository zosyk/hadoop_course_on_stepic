#! /usr/bin/python
import sys

#cat testText.txt | ./mapper.py | sort | ./reducer.py

pairs = dict()
for line in sys.stdin:

    for token in line.strip().split(" "):
        if token:
            pairs[token] = pairs.get(token,0) +1


for key, value in pairs.items():
    print(str(key) + "\t" + str(value))