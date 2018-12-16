from collections.abc import Iterable, Iterator


class Reporter(Iterable):
    def __init__(self):
        self.__key = None
        self.__key_name = None

    def set_key(self, key, name):
        self.__key = iter(key)
        self.__key_name = name

    def __iter__(self):
        return self

    def __next__(self):
        if not self.__key:
            raise StopIteration
        return next(self.__key)
