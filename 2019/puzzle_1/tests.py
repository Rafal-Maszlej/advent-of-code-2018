import pytest

from solver import calculate_fuel, calculate_total_module_fuel


def test_calculate_fuel():
    assert calculate_fuel(12) == 2
    assert calculate_fuel(14) == 2
    assert calculate_fuel(1969) == 654
    assert calculate_fuel(100756) == 33583


def test_calculate_total_module_fuel():
    assert calculate_total_module_fuel(14) == 2
    assert calculate_total_module_fuel(1969) == 966
    assert calculate_total_module_fuel(100756) == 50346


if __name__ == "__main__":
    pytest.main([__file__])
