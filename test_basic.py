def add(a, b):
    return a + b


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-1, -1) == -2


def test_add_zeros():
    assert add(0, 0) == 0


def test_add_wrong_num():
    assert add(2, 3) == 5
