def get_next_coordinates(row, col, delta_r, delta_c, max_r, max_c):
    col = (col + delta_c) % max_c
    row += delta_r

    if row >= max_r:
        row = None

    return row, col


def count_trees(grid, delta_r, delta_c):
    row, col = 0, 0
    max_r = len(grid)
    max_c = len(grid[0])

    counter = 0

    while True:
        row, col = get_next_coordinates(row, col, delta_r, delta_c, max_r, max_c)

        if row is not None:
            if grid[row][col] == "#":
                counter += 1
        else:
            return counter


if __name__ == "__main__":
    with open("input.txt") as f:
        grid = [line.strip() for line in f.readlines()]

    # puzzle 1
    assert count_trees(grid, 1, 3) == 284

    # puzzle 2
    a = count_trees(grid, 1, 1)
    b = count_trees(grid, 1, 3)
    c = count_trees(grid, 1, 5)
    d = count_trees(grid, 1, 7)
    e = count_trees(grid, 2, 1)

    assert a * b * c * d * e == 3510149120
