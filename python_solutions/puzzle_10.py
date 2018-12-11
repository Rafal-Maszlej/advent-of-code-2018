class Point:
    def __init__(self, x, y, vector_x, vector_y):
        self.x = x
        self.y = y
        self.vector_x = vector_x
        self.vector_y = vector_y

    def __repr__(self):
        return f"Point({self.x}, {self.y}, {self.vector_x}, {self.vector_y})"

    def move(self):
        self.x += self.vector_x
        self.y += self.vector_y

    @property
    def coords(self):
        return self.x, self.y


class Grid:
    EMPTY = '.'
    OCCUPIED = '#'
    DIRECTIONS = ((0, 1), (0, -1), (1, 0), (-1, 0))
    GROUP_ERROR_TOLERANCE = 50
    SIMULATION_TIME = 15000

    def __init__(self, data):
        self.points = [Point(*self.parse_input(line)) for line in data.strip().split('\n')]

    @staticmethod
    def parse_input(line):
        line = line.replace('position=<', '').replace('> velocity=<', ',').rstrip('>').split(',')
        return [int(number.strip()) for number in line]

    @property
    def min_x(self):
        return min(point.x for point in self.points)

    @property
    def max_x(self):
        return max(point.x for point in self.points)

    @property
    def min_y(self):
        return min(point.y for point in self.points)

    @property
    def max_y(self):
        return max(point.y for point in self.points)

    def get_all_coords(self):
        return [point.coords for point in self.points]

    def draw(self):
        grid = [[self.EMPTY] * (self.max_x + 1) for _ in range(self.max_y + 1)]

        for point in self.points:
            grid[point.y][point.x] = self.OCCUPIED

        for row in grid:
            print(' '.join(row))

    def have_neighbour(self, point, coords):
        next_pos = [(point.x + x, point.y + y) for x, y in self.DIRECTIONS]
        return any(pos in coords for pos in next_pos)

    def move_points(self):
        for point in self.points:
            point.move()

    def in_group(self):
        coords = self.get_all_coords()
        neighbours_amount = sum(self.have_neighbour(point, coords) for point in self.points)

        return neighbours_amount > len(coords) - self.GROUP_ERROR_TOLERANCE

    def simulate(self):
        for second in range(1, self.SIMULATION_TIME):
            self.move_points()

            if self.in_group():
                self.draw()      # part 1
                print(second)    # part 2
                return


if __name__ == '__main__':
    test_data = """position=< 9,  1> velocity=< 0,  2>
                   position=< 7,  0> velocity=<-1,  0>
                   position=< 3, -2> velocity=<-1,  1>
                   position=< 6, 10> velocity=<-2, -1>
                   position=< 2, -4> velocity=< 2,  2>
                   position=<-6, 10> velocity=< 2, -2>
                   position=< 1,  8> velocity=< 1, -1>
                   position=< 1,  7> velocity=< 1,  0>
                   position=<-3, 11> velocity=< 1, -2>
                   position=< 7,  6> velocity=<-1, -1>
                   position=<-2,  3> velocity=< 1,  0>
                   position=<-4,  3> velocity=< 2,  0>
                   position=<10, -3> velocity=<-1,  1>
                   position=< 5, 11> velocity=< 1, -2>
                   position=< 4,  7> velocity=< 0, -1>
                   position=< 8, -2> velocity=< 0,  1>
                   position=<15,  0> velocity=<-2,  0>
                   position=< 1,  6> velocity=< 1,  0>
                   position=< 8,  9> velocity=< 0, -1>
                   position=< 3,  3> velocity=<-1,  1>
                   position=< 0,  5> velocity=< 0, -1>
                   position=<-2,  2> velocity=< 2,  0>
                   position=< 5, -2> velocity=< 1,  2>
                   position=< 1,  4> velocity=< 2,  1>
                   position=<-2,  7> velocity=< 2, -2>
                   position=< 3,  6> velocity=<-1, -1>
                   position=< 5,  0> velocity=< 1,  0>
                   position=<-6,  0> velocity=< 2,  0>
                   position=< 5,  9> velocity=< 1, -2>
                   position=<14,  7> velocity=<-2,  0>
                   position=<-3,  6> velocity=< 2, -1>"""

    with open('../inputs/input_10.txt') as f:
        data = f.read()

    grid = Grid(data)
    grid.simulate()
