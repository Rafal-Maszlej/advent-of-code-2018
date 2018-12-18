class Cache:
    def __init__(self):
        self._cache = {}
        self._indexes = []

    def add(self, key, value):
        self._cache[key] = value
        self._indexes.append(key)

    def is_interval(self, key):
        return self._indexes.count(key) == 2

    def get_interval(self, key):
        start = self._indexes.index(key)
        end = self._indexes.index(key, start + 1)

        return start, end

    def compute_from_cache(self, key, index):
        start, end = self.get_interval(key)
        interval = self._indexes[start:end]

        key = interval[(index - start - 1) % len(interval)]

        return self._cache[key]


class Area:
    OPEN_GROUND = '.'
    TREES = '|'
    LUMBERYARD = '#'
    NO_AREA = '?'

    def __init__(self, data, size=50):
        self.size = size
        self.area = [list(row.strip()) for row in data.split('\n')]
        self.cache = Cache()

    def __str__(self):
        return '\n'.join(''.join(row) for row in self.area)

    def get_surrounding_cells(self, x, y):
        directions = [(1, 0), (1, 1), (1, -1), (0, 1), (-1, 0), (-1, -1), (0, -1), (-1, 1)]
        adjacent_cells = [
            self.area[y + d_y][x + d_x] for d_x, d_y in directions
            if 0 <= x + d_x < self.size and 0 <= y + d_y < self.size
        ]

        return {
            'open_area': adjacent_cells.count(self.OPEN_GROUND),
            'trees': adjacent_cells.count(self.TREES),
            'lumberyard': adjacent_cells.count(self.LUMBERYARD)
        }

    def compute_changes(self):
        new_area = [[self.NO_AREA] * self.size for _ in range(self.size)]

        for y in range(self.size):
            for x in range(self.size):
                surrounding_cells = self.get_surrounding_cells(x, y)

                if self.area[y][x] == self.OPEN_GROUND and surrounding_cells['trees'] >= 3:
                    new_area[y][x] = self.TREES
                elif self.area[y][x] == self.TREES and surrounding_cells['lumberyard'] >= 3:
                    new_area[y][x] = self.LUMBERYARD
                elif self.area[y][x] == self.LUMBERYARD:
                    if surrounding_cells['lumberyard'] >= 1 and surrounding_cells['trees'] >= 1:
                        new_area[y][x] = self.LUMBERYARD
                    else:
                        new_area[y][x] = self.OPEN_GROUND
                else:
                    new_area[y][x] = self.area[y][x]

        self.cache.add(repr(self.area), new_area)

        self.area = new_area

    def get_from_cache(self, simulation_time):
        return self.cache.compute_from_cache(repr(self.area), simulation_time)

    def simulate(self, simulation_time=10):
        for i in range(simulation_time):
            if self.cache.is_interval(repr(self.area)):
                self.area = self.get_from_cache(simulation_time)
                break

            self.compute_changes()

        area = ''.join(''.join(row) for row in self.area)

        return area.count(self.TREES) * area.count(self.LUMBERYARD)


if __name__ == '__main__':
    test_data = """.#.#...|#.
                   .....#|##|
                   .|..|...#.
                   ..|#.....#
                   #.#|||#|#|
                   ...#.||...
                   .|....|...
                   ||...#|.#|
                   |.||||..|.
                   ...#.|..|."""

    with open('input.txt') as f:
        puzzle_input = f.read()

    # part 1
    area = Area(test_data, size=10)
    assert area.simulate() == 1147

    area = Area(puzzle_input)
    assert area.simulate() == 675100

    # part 2
    area = Area(puzzle_input)
    assert area.simulate(simulation_time=1_000_000_000) == 191820
