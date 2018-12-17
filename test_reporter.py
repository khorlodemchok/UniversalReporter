import pytest
from reporter import Reporter


def test_no_key():
    r = Reporter()
    assert list(r) == []


def test_no_iterable():
    r = Reporter()
    with pytest.raises(TypeError):
        r.set_key(42, "zupa")


def test_iter():
    items = ["spam", "eggs", "sausage"]
    expected = [
        {"zupa": "spam"},
        {"zupa": "eggs"},
        {"zupa": "sausage"}
    ]
    r = Reporter()
    r.set_key(items, "zupa")
    assert list(r) == expected


def test_empty_relation():

    rel_data = {
        "spam": None
    }

    def zero(key):
        return data_func(rel_data, key)

    items = ["spam"]
    expected = [
        {
            "key": "spam",
            "rel": None
        }
    ]

    r = Reporter()
    r.set_key(items, "key")
    r.add_relation(zero, "rel")
    assert list(r) == expected


def test_one_relation():
    rel_data = {
        "spam": "spam_val",
        "eggs": "eggs_val",
        "bacon": "bacon_val"
    }

    key = [
        "spam",
        "eggs",
        "bacon"
    ]

    expected = [
        {
            "key": "spam",
            "rel1": "spam_val"
        },
        {
            "key": "eggs",
            "rel1": "eggs_val"
        },
        {
            "key": "bacon",
            "rel1": "bacon_val"
        }
    ]

    r = Reporter()
    r.set_key(key, "key")

    def f(k):
        return data_func(rel_data, k)
    r.add_relation(f, "rel1")
    assert list(r) == expected


def test_multiple_relations():
    keys = ["spam"]
    rel1 = {
        "spam": "spam_rel1"
    }
    rel2 = {
        "spam": "spam_rel2"
    }
    expected = [
        {
            "key": "spam",
            "rel1": "spam_rel1",
            "rel2": "spam_rel2"
        }
    ]

    def f_rel1(k):
        return data_func(rel1, k)

    def f_rel2(k):
        return data_func(rel2, k)

    r = Reporter()
    r.set_key(keys, "key")
    r.add_relation(f_rel1, "rel1")
    r.add_relation(f_rel2, "rel2")

    result = list(r)
    assert result == expected


def data_func(rel_data, k):
    return rel_data[k]
