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
    def zero(_):
        return None

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
    reldata = {
        "spam": "spam_val",
        "eggs": "eggs_val",
        "bacon": "bacon_val"
    }

    def data_func(k):
        return reldata[k]

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
    r.add_relation(data_func, "rel1")
    assert list(r) == expected
