from copy import deepcopy
from itertools import cycle
from typing import List


class GameOfLife:
    EMPTY = "L"
    OCCUPIED = "#"
    FLOOR = "."

    def __init__(self):
        self.state = []

    def get_adjacent_cells(self, row, col):
        adjacent_cells = []

        max_col = len(self.state[0]) - 1
        max_row = len(self.state) - 1

        if row > 0:
            if col == 0:
                adjacent_cells.extend(self.state[row-1][col:col+2])
            elif col == max_col:
                adjacent_cells.extend(self.state[row-1][col-1:col+1])
            else:
                adjacent_cells.extend(self.state[row-1][col-1:col+2])

        if col > 0:
            adjacent_cells.append(self.state[row][col-1])

        if col < max_col:
            adjacent_cells.append(self.state[row][col+1])

        if row < max_row:
            if col == 0:
                adjacent_cells.extend(self.state[row+1][col:col+2])
            elif col == max_col:
                adjacent_cells.extend(self.state[row+1][col-1:col+1])
            else:
                adjacent_cells.extend(self.state[row+1][col-1:col+2])

        return adjacent_cells

    def get_new_cell_state(self, row, col):
        adjacent_cells = self.get_adjacent_cells(row, col)
        cell = self.state[row][col]

        if cell == self.EMPTY and self.OCCUPIED not in adjacent_cells:
            return self.OCCUPIED
        elif cell == self.OCCUPIED and adjacent_cells.count(self.OCCUPIED) >= 4:
            return self.EMPTY
        else:
            return cell

    def get_occupied_seats(self):
        return sum(row.count(self.OCCUPIED) for row in self.state)

    def load(self, data: str):
        self.state = parse_data(data)

    def compute_next_state(self):
        temp_grid = deepcopy(self.state)

        for row in range(len(self.state)):
            for col in range(len(self.state[0])):
                new_state = self.get_new_cell_state(row, col)
                temp_grid[row][col] = new_state

        return temp_grid

    def run(self):
        while True:
            state = self.compute_next_state()

            if state != self.state:
                self.state = state
            else:
                return


class GameOfLifeExtended(GameOfLife):
    def get_direction_cell(self, direction, row, col):
        max_row = len(self.state)
        max_col = len(self.state[0])

        if direction == 0:
            row_range = range(row, -1, -1)
            col_range = range(col, -1, -1)
        elif direction == 1:
            row_range = range(row, -1, -1)
            col_range = cycle([col])
        elif direction == 2:
            row_range = range(row, -1, -1)
            col_range = range(col, max_col)
        elif direction == 3:
            row_range = cycle([row])
            col_range = range(col, -1, -1)
        elif direction == 4:
            row_range = cycle([row])
            col_range = range(col, max_col)
        elif direction == 5:
            row_range = range(row, max_row)
            col_range = range(col, -1, -1)
        elif direction == 6:
            row_range = range(row, max_row)
            col_range = cycle([col])
        elif direction == 7:
            row_range = range(row, max_row)
            col_range = range(col, max_col)
        else:
            return

        cells = [self.state[r][c] for r, c in zip(row_range, col_range)]
        cells = "".join(cells).replace(".", "")

        if len(cells) > 1:
            return cells[1]

    def get_adjacent_cells(self, row, col):
        adjacent_cells = []

        for direction in range(8):
            cell = self.get_direction_cell(direction, row, col)
            if cell is not None:
                adjacent_cells.append(cell)

        return adjacent_cells

    def get_new_cell_state(self, row, col):
        adjacent_cells = self.get_adjacent_cells(row, col)
        cell_state = self.state[row][col]

        if cell_state == self.EMPTY and self.OCCUPIED not in adjacent_cells:
            return self.OCCUPIED
        elif cell_state == self.OCCUPIED and adjacent_cells.count(self.OCCUPIED) >= 5:
            return self.EMPTY
        else:
            return cell_state


def parse_data(data: str) -> List[List[str]]:
    data = data.strip().split("\n")
    return [list(row.strip()) for row in data]


if __name__ == "__main__":
    import pytest

    pytest.main()

    with open("input.txt") as f:
        data = f.read()

    # puzzle 1
    game_of_life = GameOfLife()
    game_of_life.load(data)
    game_of_life.run()

    occupied_seats = game_of_life.get_occupied_seats()
    assert occupied_seats == 2194

    # puzzle 2
    game_of_life = GameOfLifeExtended()
    game_of_life.load(data)
    game_of_life.run()

    occupied_seats = game_of_life.get_occupied_seats()
    assert occupied_seats == 1944
