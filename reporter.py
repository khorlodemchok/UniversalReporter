from collections.abc import Iterable


class Reporter(Iterable):
    def __init__(self):
        self.__key = None
        self.__key_name = None
        self.__rel = []
        self.__rel_name = []

    def set_key(self, key, name):
        self.__key = iter(key)
        self.__key_name = name

    def add_relation(self, func, name):
        self.__rel.append(func)
        self.__rel_name.append(name)

    def add_relation_multi(self, func, names):

        def mk_func(f, i):
            def new_func(key):
                return f(key)[i]
            return new_func

        for n in range(0, len(names)):

            self.__rel.append(mk_func(func, n))
            self.__rel_name.append(names[n])

    def __iter__(self):
        return self

    def __next__(self):
        if not self.__key:
            raise StopIteration
        result = dict()
        key = next(self.__key)
        result[self.__key_name] = key
        for f, n in zip(self.__rel, self.__rel_name):
            result[n] = f(key)
        return result
