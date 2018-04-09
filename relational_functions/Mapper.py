#!/usr/bin/python
import sys


class User:

    def __init__(self, created_timestamp, id, url):
        self.__created_timestamp = created_timestamp
        self.__id = id
        self.__url = url

    def get_id(self):
        return self.__id

    def __str__(self):
        return self.__created_timestamp + "\t" + self.__id + "\t" + self.__url


class Mapper:

    def map(self, line):
        (created_timestamp, id, url) = line.strip().split("\t")
        user = User(created_timestamp, id, url)

        if(user.get_id() == "user10"):
            print(user)


def main():
    mapper = Mapper()
    for line in sys.stdin:
        mapper.map(line)


main()
