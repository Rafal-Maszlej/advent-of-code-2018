import pytest

from solver import NavigationComputerExtended, Direction


@pytest.fixture
def navigation_computer():
    return NavigationComputerExtended()


def test_move_north_action(navigation_computer):
    navigation_computer.move_north(10)
    assert navigation_computer.waypoint_x == 10
    assert navigation_computer.waypoint_y == 11


def test_move_south_action(navigation_computer):
    navigation_computer.move_south(10)
    assert navigation_computer.waypoint_x == 10
    assert navigation_computer.waypoint_y == -9


def test_move_east_action(navigation_computer):
    navigation_computer.move_east(10)
    assert navigation_computer.waypoint_x == 20
    assert navigation_computer.waypoint_y == 1


def test_move_west_action(navigation_computer):
    navigation_computer.move_west(10)
    assert navigation_computer.waypoint_x == 0
    assert navigation_computer.waypoint_y == 1


@pytest.mark.parametrize(
    ["angle", "expected_x", "expected_y"],
    [
        [90, -1, 10],
        [180, -10, -1],
        [270, 1, -10],
        [450, -1, 10]
    ]
)
def test_turn_left_action(angle, expected_x, expected_y, navigation_computer):
    navigation_computer.turn_left(angle)
    assert navigation_computer.waypoint_x == expected_x
    assert navigation_computer.waypoint_y == expected_y


@pytest.mark.parametrize(
    ["angle", "expected_x", "expected_y"],
    [
        [90, 1, -10],
        [180, -10, -1],
        [270, -1, 10],
        [450, 1, -10]
    ]
)
def test_turn_right_action(angle, expected_x, expected_y, navigation_computer):
    navigation_computer.turn_right(angle)
    assert navigation_computer.waypoint_x == expected_x
    assert navigation_computer.waypoint_y == expected_y


@pytest.mark.parametrize(
    ["distance", "expected_x", "expected_y"],
    [
        [10, 100, 10],
        [7, 70, 7]
    ]
)
def test_move_forward(distance, expected_x, expected_y, navigation_computer):
    navigation_computer.move_forward(distance)
    assert navigation_computer.x == expected_x
    assert navigation_computer.y == expected_y
