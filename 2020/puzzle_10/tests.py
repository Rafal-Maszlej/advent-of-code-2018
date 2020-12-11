import pytest

from solver import joltage_difference, combinations_count


@pytest.fixture
def data_small():
    return [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]


@pytest.fixture
def data_large():
    return [
        28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24,
        23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35,
        8, 17, 7, 9, 4, 2, 34, 10, 3
    ]


def test_joltage_difference_small(data_small):
    result = joltage_difference(data_small)
    assert result == 35


def test_joltage_difference_large(data_large):
    result = joltage_difference(data_large)
    assert result == 220


def test_combinations_count_small(data_small):
    result = combinations_count(data_small)
    assert result == 8


# def test_combinations_count_large(data_large):
#     result = combinations_count(data_large)
#     assert result == 19208


if __name__ == "__main__":
    pytest.main([__file__])
