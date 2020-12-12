import pytest

from solver import NavigationComputer, Direction


@pytest.fixture
def navigation_computer():
    return NavigationComputer()


def test_move_north_action(navigation_computer):
    navigation_computer.move_north(10)
    assert navigation_computer.x == 0
    assert navigation_computer.y == 10


def test_move_south_action(navigation_computer):
    navigation_computer.move_south(10)
    assert navigation_computer.x == 0
    assert navigation_computer.y == -10


def test_move_east_action(navigation_computer):
    navigation_computer.move_east(10)
    assert navigation_computer.x == 10
    assert navigation_computer.y == 0


def test_move_west_action(navigation_computer):
    navigation_computer.move_west(10)
    assert navigation_computer.x == -10
    assert navigation_computer.y == 0


@pytest.mark.parametrize(
    ["angle", "expected_direction"],
    [
        [90, Direction.NORTH],
        [180, Direction.WEST],
        [270, Direction.SOUTH],
        [450, Direction.NORTH]
    ]
)
def test_turn_left_action(angle, expected_direction, navigation_computer):
    navigation_computer.turn_left(angle)
    assert navigation_computer.direction == expected_direction


@pytest.mark.parametrize(
    ["angle", "expected_direction"],
    [
        [90, Direction.SOUTH],
        [180, Direction.WEST],
        [270, Direction.NORTH],
        [450, Direction.SOUTH]
    ]
)
def test_turn_right_action(angle, expected_direction, navigation_computer):
    navigation_computer.turn_right(angle)
    assert navigation_computer.direction == expected_direction


@pytest.mark.parametrize(
    ["direction", "expected_x", "expected_y"],
    [
        [Direction.EAST, 10, 0],
        [Direction.WEST, -10, 0],
        [Direction.NORTH, 0, 10],
        [Direction.SOUTH, 0, -10]
    ]
)
def test_move_forward_action(direction, expected_x, expected_y, navigation_computer):
    navigation_computer.direction = direction
    navigation_computer.move_forward(10)
    assert navigation_computer.x == expected_x
    assert navigation_computer.y == expected_y


def test_run(navigation_computer, data):
    navigation_computer.run(data)
    assert navigation_computer.x == 17
    assert navigation_computer.y == -8


@pytest.mark.parametrize(
    ["x", "y", "expected_distance"],
    [
        [0, 0, 0],
        [3, 7, 10],
        [17, -8, 25],
        [-9, 3, 12],
        [-3, -5, 8]
    ]
)
def test_get_total_distance(x, y, expected_distance, navigation_computer):
    navigation_computer.x = x
    navigation_computer.y = y
    distance = navigation_computer.get_total_distance()
    assert distance == expected_distance
