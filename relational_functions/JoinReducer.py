#!/usr/bin/python

import sys


class User:
    __id = None
    __query = None
    __url = None

    def __init__(self, id, query, url):
        self.__id = id
        self.__query = query
        self.__url = url

    def __str__(self):
        return self.__id + "\t" + self.__query + "\t" + self.__url


class Reducer:

    def __init__(self):
        self.__queries = []
        self.__urls = []
        self.__users = []

    def reduce(self, line):
        queries = self.__queries
        urls = self.__urls

        (id, query_or_url) = line.strip().split("\t")

        (key, value) = query_or_url.strip().split(":")

        if key == "query":
            queries.append((id, value))
        elif key == "url":
            urls.append((id, value))

    def close(self):
        queries = self.__queries
        urls = self.__urls

        for (q_id, query) in queries:
            for (u_id, url) in urls:
                if q_id == u_id:
                    print(User(q_id, query, url))


def main():
    reducer = Reducer()
    for line in sys.stdin:
        reducer.reduce(line)
    reducer.close()


main()
