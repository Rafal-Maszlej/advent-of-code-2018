import pytest

from solver import parse_data, GameOfLife


@pytest.fixture
def game_of_life():
    return GameOfLife()


@pytest.fixture
def data_small():
    return """
L..L
.#.L
L##.
.L.L"""


@pytest.fixture
def data_next_state():
    data = """#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##"""
    return parse_data(data)


@pytest.fixture
def data_final_state():
    data = """#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##"""
    return parse_data(data)


def test_load(game_of_life, data_small):
    expected_data = [
        ["L", ".", ".", "L"],
        [".", "#", ".", "L"],
        ["L", "#", "#", "."],
        [".", "L", ".", "L"]
    ]
    game_of_life.load(data_small)
    assert game_of_life.state == expected_data


@pytest.mark.parametrize(
    ["row", "col", "expected_adjacent_cells"],
    [
        [1, 1, ["L", ".", ".", ".", ".", "L", "#", "#"]],
        [2, 1, [".", "#", ".", "L", "#", ".", "L", "."]],
        [0, 1, ["L", ".", ".", "#", "."]],
        [1, 3, [".", "L", ".", "#", "."]],
        [0, 0, [".", ".", "#"]],
        [3, 3, ["#", ".", "."]]
    ]
)
def test_get_adjacent_cells(row, col, expected_adjacent_cells, game_of_life, data_small):
    game_of_life.load(data_small)
    adjacent_cells = game_of_life.get_adjacent_cells(row=row, col=col)
    assert adjacent_cells == expected_adjacent_cells


def test_compute_next_round(game_of_life, data_initial, data_next_state):
    game_of_life.load(data_initial)
    next_state = game_of_life.compute_next_state()
    assert next_state == data_next_state


def test_run(game_of_life, data_initial, data_final_state):
    game_of_life.load(data_initial)
    game_of_life.run()
    assert game_of_life.state == data_final_state
