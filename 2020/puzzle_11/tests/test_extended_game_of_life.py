import pytest

from solver import parse_data, GameOfLifeExtended


@pytest.fixture
def game_of_life():
    return GameOfLifeExtended()


def state_1():
    data = """.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#....."""
    return parse_data(data)


def state_2():
    data = """.............
.L.L.#.#.#.#.
............."""
    return parse_data(data)


def state_3():
    data = """.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##."""
    return parse_data(data)


@pytest.fixture
def data_final_state():
    data = """#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.LL.L#
#.LLLL#.LL
..#.L.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#"""
    return parse_data(data)


@pytest.mark.parametrize(
    ["direction", "r", "c"],
    [
        [0, 2, 1],
        [1, 1, 3],
        [2, 0, 7],
        [3, 4, 2],
        [4, 4, 8],
        [5, 7, 0],
        [6, 8, 3],
        [7, 5, 4]
    ]
)
def test_get_direction_cell(direction, r, c, game_of_life):
    row, col = 4, 3
    game_of_life.state = state_1()
    game_of_life.state[r][c] = "L"
    cell = game_of_life.get_direction_cell(direction, row, col)
    assert cell == "L"


@pytest.mark.parametrize(
    ["row", "col", "state", "expected_cells"],
    [
        [4, 3, state_1(), ["#", "#", "#", "#", "#", "#", "#", "#"]],
        [1, 1, state_2(), ["L"]],
        [3, 3, state_3(), []]
    ]
)
def test_get_adjacent_cells(row, col, state, expected_cells, game_of_life):
    game_of_life.state = state
    adjacent_cells = game_of_life.get_adjacent_cells(row=row, col=col)
    assert adjacent_cells == expected_cells


def test_run(game_of_life, data_initial, data_final_state):
    game_of_life.load(data_initial)
    game_of_life.run()
    assert game_of_life.state == data_final_state
