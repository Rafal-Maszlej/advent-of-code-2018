class Wire:
    def __init__(self):
        self.points = [(0, 0)]

    @staticmethod
    def get_direction_modifier(direction):
        return {
            "U": (0, 1),
            "D": (0, -1),
            "R": (1, 0),
            "L": (-1, 0)
        }.get(direction, (0, 0))

    def add_points(self, points_data):
        x, y = self.points[-1][0], self.points[-1][1]
        x_mod, y_mod = self.get_direction_modifier(points_data[0])
        distance = int(points_data[1:])

        self.points.extend([(x + x_mod * i, y + y_mod * i) for i in range(1, distance + 1)])


class Area:
    CENTRAL_PORT = (0, 0)

    def __init__(self):
        self.wires = dict()

    def add_wire(self, wire_id, wire_data):
        wire = Wire()

        for point in wire_data:
            wire.add_points(point)

        self.wires[wire_id] = wire

    def get_intersections(self, wire_1_id, wire_2_id):
        wire1 = self.wires.get(wire_1_id)
        wire2 = self.wires.get(wire_2_id)

        intersections = set(wire1.points).intersection(set(wire2.points))
        intersections.remove(Area.CENTRAL_PORT)

        return intersections

    def get_distance_to_point(self, wire_id, point):
        return self.wires[wire_id].points.index(point)

    def get_closest_intersection_distance(self, wire_1_id, wire_2_id):
        intersection = self.get_intersections(wire_1_id, wire_2_id)

        return min(manhattan_distance(Area.CENTRAL_PORT, point) for point in intersection)

    def get_fewer_combined_intersection_distance(self, wire_1_id, wire_2_id):
        intersection = self.get_intersections(wire_1_id, wire_2_id)

        wire_1_distances = [self.get_distance_to_point(wire_1_id, point) for point in intersection]
        wire_2_distances = [self.get_distance_to_point(wire_2_id, point) for point in intersection]

        return min(dist1 + dist2 for dist1, dist2 in zip(wire_1_distances, wire_2_distances))


def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


if __name__ == "__main__":
    with open("input.txt") as f:
        wire_1_data, wire_2_data = f.read().strip().split("\n")

    wire_1_id = 1
    wire_1_data = wire_1_data.split(",")

    wire_2_id = 2
    wire_2_data = wire_2_data.split(",")

    area = Area()

    area.add_wire(wire_1_id, wire_1_data)
    area.add_wire(wire_2_id, wire_2_data)

    #  Part 1
    closest_intersection_distance = area.get_closest_intersection_distance(wire_1_id, wire_2_id)
    assert closest_intersection_distance == 1195

    #  Part 2
    fewer_combined_intersection_distance = area.get_fewer_combined_intersection_distance(wire_1_id, wire_2_id)
    assert fewer_combined_intersection_distance == 91518
