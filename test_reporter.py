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


def test_multi_multi_rel():
    keys = ["spam"]
    rel_data = {
        "spam": ["eggs", "bacon"]
    }

    expected = [
        {
            "key": "spam",
            "rel1": "eggs",
            "rel2": "bacon"
        }
    ]

    def f_rel(k):
        return rel_data[k]

    r = Reporter()
    r.set_key(keys, "key")
    r.add_relation_multi(f_rel, ["rel1", "rel2"])

    result = list(r)
    print(result)
    assert result == expected
