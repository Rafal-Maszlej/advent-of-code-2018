import pytest

from solver import get_paper_surface, get_ribbon_length


def test_get_paper_surface():
    assert get_paper_surface("2x3x4") == 58
    assert get_paper_surface("1x1x10") == 43


def test_get_ribbon_length():
    assert get_ribbon_length("2x3x4") == 34
    assert get_ribbon_length("1x1x10") == 14


if __name__ == "__main__":
    pytest.main([__file__])
