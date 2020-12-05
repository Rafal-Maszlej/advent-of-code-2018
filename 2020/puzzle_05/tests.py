import pytest

from solver import Zone, get_seat_id


@pytest.fixture
def zone():
    return Zone()


@pytest.mark.parametrize(
    ["min_row", "max_row", "expected_max_row"],
    [
        (0, 127, 63),
        (32, 63, 47),
        (44, 47, 45),
        (44, 45, 44),
    ]
)
def test_zone_front(min_row, max_row, expected_max_row, zone):
    zone.min_row = min_row
    zone.max_row = max_row

    zone.front()

    assert zone.max_row == expected_max_row


@pytest.mark.parametrize(
    ["min_row", "max_row", "expected_min_row"],
    [
        (0, 63, 32),
        (32, 47, 40),
        (40, 47, 44),
    ]
)
def test_zone_back(min_row, max_row, expected_min_row, zone):
    zone.min_row = min_row
    zone.max_row = max_row

    zone.back()

    assert zone.min_row == expected_min_row


@pytest.mark.parametrize(
    ["min_col", "max_col", "expected_min_col"],
    [
        (0, 7, 4),
        (4, 5, 5)
    ]
)
def test_zone_right(min_col, max_col, expected_min_col, zone):
    zone.min_col = min_col
    zone.max_col = max_col

    zone.right()

    assert zone.min_col == expected_min_col


@pytest.mark.parametrize(
    ["min_col", "max_col", "expected_max_col"],
    [
        (4, 7, 5)
    ]
)
def test_zone_left(min_col, max_col, expected_max_col, zone):
    zone.min_col = min_col
    zone.max_col = max_col

    zone.left()

    assert zone.max_col == expected_max_col


@pytest.mark.parametrize(
    [
        "min_row",
        "max_row",
        "min_col",
        "max_col",
        "code",
        "expected_min_row",
        "expected_max_row",
        "expected_min_col",
        "expected_max_col"
    ],
    [
        (0, 127, 0, 7, "F", 0, 63, 0, 7),
        (0, 63, 0, 7, "B", 32, 63, 0, 7),
        (32, 63, 0, 7, "F", 32, 47, 0, 7),
        (32, 47, 0, 7, "B", 40, 47, 0, 7),
        (40, 47, 0, 7, "B", 44, 47, 0, 7),
        (44, 47, 0, 7, "F", 44, 45, 0, 7),
        (44, 45, 0, 7, "F", 44, 44, 0, 7),
        (44, 44, 0, 7, "R", 44, 44, 4, 7),
        (44, 44, 4, 7, "L", 44, 44, 4, 5),
        (44, 44, 4, 5, "R", 44, 44, 5, 5)
    ]
)
def test_update_zone(
        min_row,
        max_row,
        min_col,
        max_col,
        code,
        expected_min_row,
        expected_max_row,
        expected_min_col,
        expected_max_col,
        zone
):
    zone.min_row = min_row
    zone.max_row = max_row
    zone.min_col = min_col
    zone.max_col = max_col

    zone.update(code)

    assert zone.min_row == expected_min_row
    assert zone.max_row == expected_max_row
    assert zone.min_col == expected_min_col
    assert zone.max_col == expected_max_col


@pytest.mark.parametrize(
    ["boarding_pass", "expected_seat_id"],
    [
        ("BFFFBBFRRR", 567),
        ("FFFBBBFRRR", 119),
        ("BBFFBBFRLL", 820),
    ]
)
def test_get_seat_id(boarding_pass, expected_seat_id):
    seat_id = get_seat_id(boarding_pass)
    assert seat_id == expected_seat_id


if __name__ == "__main__":
    pytest.main([__file__])
