#!/usr/bin/python
import sys
import re



class Mapper:

    def map(self, line):
        (word, doc_id, word_count) = line.strip().split("\t")
        print(word + "\t" + doc_id + ";" + word_count + ";1")


def main():
    mapper = Mapper()
    for line in sys.stdin:
        mapper.map(line)


main()
