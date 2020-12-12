from enum import Enum


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class NavigationComputer:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = Direction.EAST

    def move_north(self, distance):
        self.y += distance

    def move_south(self, distance):
        self.y -= distance

    def move_east(self, distance):
        self.x += distance

    def move_west(self, distance):
        self.x -= distance

    def turn_left(self, angle):
        new_direction = Direction((self.direction.value - angle // 90) % 4)
        self.direction = new_direction

    def turn_right(self, angle):
        new_direction = Direction((self.direction.value + angle // 90) % 4)
        self.direction = new_direction

    def move_forward(self, distance):
        if self.direction == Direction.NORTH:
            self.y += distance
        elif self.direction == Direction.EAST:
            self.x += distance
        elif self.direction == Direction.SOUTH:
            self.y -= distance
        elif self.direction == Direction.WEST:
            self.x -= distance

    def get_action(self, action: str):
        actions = {
            "N": self.move_north,
            "S": self.move_south,
            "E": self.move_east,
            "W": self.move_west,
            "L": self.turn_left,
            "R": self.turn_right,
            "F": self.move_forward
        }
        return actions.get(action)

    def get_total_distance(self):
        return abs(self.x) + abs(self.y)

    def run(self, data):
        for row in data:
            action = self.get_action(row[0])
            value = int(row[1:])

            action(value)


class NavigationComputerExtended(NavigationComputer):
    def __init__(self):
        super().__init__()
        self.waypoint_x = 10
        self.waypoint_y = 1

    def move_north(self, distance):
        self.waypoint_y += distance

    def move_south(self, distance):
        self.waypoint_y -= distance

    def move_east(self, distance):
        self.waypoint_x += distance

    def move_west(self, distance):
        self.waypoint_x -= distance

    def turn_left(self, angle):
        angle = angle // 90 % 4

        if angle == 1:
            _x = -self.waypoint_y
            _y = self.waypoint_x
        elif angle == 2:
            _x = -self.waypoint_x
            _y = -self.waypoint_y
        elif angle == 3:
            _x = self.waypoint_y
            _y = -self.waypoint_x
        else:
            _x = 0
            _y = 0

        self.waypoint_x = _x
        self.waypoint_y = _y

    def turn_right(self, angle):
        angle = angle // 90 % 4

        if angle == 1:
            _x = self.waypoint_y
            _y = -self.waypoint_x
        elif angle == 2:
            _x = -self.waypoint_x
            _y = -self.waypoint_y
        elif angle == 3:
            _x = -self.waypoint_y
            _y = self.waypoint_x
        else:
            _x = 0
            _y = 0

        self.waypoint_x = _x
        self.waypoint_y = _y

    def move_forward(self, distance):
        self.x += self.waypoint_x * distance
        self.y += self.waypoint_y * distance


if __name__ == "__main__":
    import pytest

    pytest.main()

    with open("input.txt") as f:
        data = f.readlines()

    # puzzle 1
    navigation_computer = NavigationComputer()
    navigation_computer.run(data)
    distance = navigation_computer.get_total_distance()
    assert distance == 319

    # puzzle 2
    navigation_computer = NavigationComputerExtended()
    navigation_computer.run(data)
    distance = navigation_computer.get_total_distance()
    assert distance == 50157
