import pytest

from solver import advent_coin_calculate


def test_advent_coin_calculate_1():
    data = "abcdef"
    expected_number = 609043
    calculated_number = advent_coin_calculate(data)

    assert calculated_number == expected_number


def test_advent_coin_calculate_2():
    data = "pqrstuv"
    expected_number = 1048970
    calculated_number = advent_coin_calculate(data)

    assert calculated_number == expected_number


if __name__ == "__main__":
    pytest.main([__file__])
