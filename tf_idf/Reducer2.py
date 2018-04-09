#!/usr/bin/python
import sys
import re


class Word:

    def __init__(self, name):
        self.__name = name
        self.__documents = []

    def put_document(self, document):
        self.__documents.append(document)

    def get_documents(self):
        return self.__documents


class Reducer:

    def __init__(self):
        self.__words = {}

    def reduce(self, line):
        words = self.__words

        (word_name, doc_id, word_count, one) = re.sub('(\W)+', " ", line).strip().split(" ")
        word = words.get(word_name, Word(word_name))

        word.put_document((doc_id, word_count))
        words[word_name] = word

    def close(self):
        words = self.__words

        for key in sorted(words.keys()):
            word = words.get(key)
            documents = word.get_documents()

            for document in documents:
                print(key + "#" + str(document[0]) + "\t" + str(document[1]) + "\t" + str(len(documents)))


def main():
    reducer = Reducer()
    for line in sys.stdin:
        reducer.reduce(line)
    reducer.close()

main()
