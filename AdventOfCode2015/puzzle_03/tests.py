import pytest

from solver import coords_calc, coords_calc_splited_data


def test_coords_number_calc():
    assert len(coords_calc(">")) == 2
    assert len(coords_calc("^>v<")) == 4
    assert len(coords_calc("^v^v^v^v^v")) == 2


def test_coords_number_calc_splited_data():
    assert len(coords_calc_splited_data("^v")) == 3
    assert len(coords_calc_splited_data("^>v<")) == 3
    assert len(coords_calc_splited_data("^v^v^v^v^v")) == 11


if __name__ == "__main__":
    pytest.main([__file__])
