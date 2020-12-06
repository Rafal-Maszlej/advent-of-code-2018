import pytest

from solver import get_floor, get_basement_at


def test_get_floor():
    assert get_floor("(())") == 0
    assert get_floor("()()") == 0
    assert get_floor("(((") == 3
    assert get_floor("(()(()(") == 3
    assert get_floor("))(((((") == 3
    assert get_floor("())") == -1
    assert get_floor("))(") == -1
    assert get_floor(")))") == -3
    assert get_floor(")())())") == -3


def test_get_basement_at():
    assert get_basement_at(")") == 1
    assert get_basement_at("()())") == 5


if __name__ == "__main__":
    pytest.main([__file__])
