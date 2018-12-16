from collections.abc import Iterable, Iterator


class Reporter(Iterable):
    def __init__(self):
        self.__key = None

    def set_key(self, k, name):
        self.__key = iter(k)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.__key:
            raise StopIteration
        return next(self.__key)
