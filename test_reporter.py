from reporter import Reporter


def test_no_key():
    r = Reporter()
    assert list(r) == []


def test_iter():
    items = ["spam", "eggs", "sausage"]
    r = Reporter()
    r.set_key(items)
    assert list(r) == items
