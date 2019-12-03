import pytest

from solver import Area, Wire


@pytest.fixture
def wire():
    return Wire()


@pytest.fixture
def area():
    area = Area()
    area.add_wire(0, ["U5", "R5", "D5"])
    return area


def test_add_points_direction_up(wire):
    direction = "U5"
    expected_points = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5)]

    wire.add_points(direction)

    assert wire.points == expected_points


def test_add_points_direction_down(wire):
    direction = "D5"
    expected_points = [(0, 0), (0, -1), (0, -2), (0, -3), (0, -4), (0, -5)]

    wire.add_points(direction)

    assert wire.points == expected_points


def test_add_points_direction_right(wire):
    direction = "R5"
    expected_points = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0)]

    wire.add_points(direction)

    assert wire.points == expected_points


def test_add_points_direction_left(wire):
    direction = "L5"
    expected_points = [(0, 0), (-1, 0), (-2, 0), (-3, 0), (-4, 0), (-5, 0)]

    wire.add_points(direction)

    assert wire.points == expected_points


def test_correct_current_location_coordinates(wire):
    wire.add_points("U5")
    wire.add_points("R10")

    assert wire.points[-1][0] == 10
    assert wire.points[-1][1] == 5


def test_closest_intersection_1(area):
    wire_1_data = "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(",")
    wire_2_data = "U62,R66,U55,R34,D71,R55,D58,R83".split(",")

    area.add_wire(1, wire_1_data)
    area.add_wire(2, wire_2_data)

    expected_distance = 159
    computed_distance = area.get_closest_intersection_distance(1, 2)

    assert computed_distance == expected_distance


def test_closest_intersection_2(area):
    wire_1_data = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(",")
    wire_2_data = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(",")

    area.add_wire(1, wire_1_data)
    area.add_wire(2, wire_2_data)

    expected_distance = 135
    computed_distance = area.get_closest_intersection_distance(1, 2)

    assert computed_distance == expected_distance


def test_get_distance_to_point(area):
    distance_to_point = area.get_distance_to_point(0, (4, 5))

    assert distance_to_point == 9


def test_fewer_combined_intersection_distance_1(area):
    wire_1_data = "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(",")
    wire_2_data = "U62,R66,U55,R34,D71,R55,D58,R83".split(",")

    area.add_wire(1, wire_1_data)
    area.add_wire(2, wire_2_data)

    expected_distance = 610
    computed_distance = area.get_fewer_combined_intersection_distance(1, 2)

    assert computed_distance == expected_distance


def test_fewer_combined_intersection_distance_2(area):
    wire_1_data = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(",")
    wire_2_data = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(",")

    area.add_wire(1, wire_1_data)
    area.add_wire(2, wire_2_data)

    expected_distance = 410
    computed_distance = area.get_fewer_combined_intersection_distance(1, 2)

    assert computed_distance == expected_distance


if __name__ == "__main__":
    pytest.main([__file__])
