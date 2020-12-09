import pytest

from solver import find_first_invalid_number, find_contiguous_numbers


@pytest.fixture
def data():
    return [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]


def test_find_first_invalid_number(data):
    number = find_first_invalid_number(data, preamble=5)
    assert number == 127


def test_find_contiguous_numbers(data):
    numbers = find_contiguous_numbers(data, number=127)
    assert numbers == [15, 25, 47, 40]


if __name__ == "__main__":
    pytest.main([__file__])
