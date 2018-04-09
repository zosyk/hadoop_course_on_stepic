#!/usr/bin/python
import sys



class Reducer:

    def __init__(self):
        self.__words = {}

    def reduce(self, line):
        words = self.__words
        (key, value) = line.strip().split("\t")
        words[key] = words.get(key, 0) + int(value)

    def close(self):
        words = self.__words

        for key in sorted(words.keys()):
            (word, doc_id) = key.strip().split("#")
            print(word + "\t" + doc_id + "\t" + str(words.get(key)))


def main():
    reducer = Reducer()
    for line in sys.stdin:
        reducer.reduce(line)

    reducer.close()

main()
