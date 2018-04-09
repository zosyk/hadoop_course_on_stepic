#!/usr/bin/python
import sys
import re



class Mapper:

    def map(self, line):
        words = re.sub('(\W)+', " ", line).strip().split(" ")
        doc_id = words.pop(0)

        for word in words:
            print(word + "#" + doc_id + "\t1")


def main():
    mapper = Mapper()
    for line in sys.stdin:
        mapper.map(line)


main()
