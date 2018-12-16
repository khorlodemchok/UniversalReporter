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
