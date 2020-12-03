import pytest

from solver import count_trees, get_next_coordinates


def test_get_coordinates_simple():
    delta_r, delta_c = 1, 3
    max_r, max_c = 12, 10

    assert get_next_coordinates(0, 0, delta_r, delta_c, max_r, max_c) == (1, 3)
    assert get_next_coordinates(1, 3, delta_r, delta_c, max_r, max_c) == (2, 6)
    assert get_next_coordinates(2, 6, delta_r, delta_c, max_r, max_c) == (3, 9)


def test_get_coordinates_right_edge():
    delta_r, delta_c = 1, 3
    max_r, max_c = 12, 10

    assert get_next_coordinates(3, 9, delta_r, delta_c, max_r, max_c) == (4, 2)
    assert get_next_coordinates(6, 8, delta_r, delta_c, max_r, max_c) == (7, 1)
    assert get_next_coordinates(9, 7, delta_r, delta_c, max_r, max_c) == (10, 0)


def test_get_coordinates_bottom_edge():
    delta_r, delta_c = 1, 3
    max_r, max_c = 12, 10

    assert get_next_coordinates(11, 3, delta_r, delta_c, max_r, max_c) == (None, 6)


def test_count_trees_simple():
    grid = [
        "..##.........##.........##.......",
        "#...#...#..#...#...#..#...#...#..",
        ".#....#..#..#....#..#..#....#..#.",
        "..#.#...#.#..#.#...#.#..#.#...#.#",
        ".#...##..#..#...##..#..#...##..#.",
        "..#.##.......#.##.......#.##.....",
        ".#.#.#....#.#.#.#....#.#.#.#....#",
        ".#........#.#........#.#........#",
        "#.##...#...#.##...#...#.##...#...",
        "#...##....##...##....##...##....#",
        ".#..#...#.#.#..#...#.#.#..#...#.#",
    ]
    assert count_trees(grid, 1, 3) == 7


def test_count_trees_complex():
    grid = [
        "..##.........##.........##.......",
        "#...#...#..#...#...#..#...#...#..",
        ".#....#..#..#....#..#..#....#..#.",
        "..#.#...#.#..#.#...#.#..#.#...#.#",
        ".#...##..#..#...##..#..#...##..#.",
        "..#.##.......#.##.......#.##.....",
        ".#.#.#....#.#.#.#....#.#.#.#....#",
        ".#........#.#........#.#........#",
        "#.##...#...#.##...#...#.##...#...",
        "#...##....##...##....##...##....#",
        ".#..#...#.#.#..#...#.#.#..#...#.#",
        "..##.........##.........##.......",
        "#...#...#..#...#...#..#...#...#..",
        ".#....#..#..#....#..#..#....#..#.",
        "..#.#...#.#..#.#...#.#..#.#...#.#",
        ".#...##..#..#...##..#..#...##..#.",
        "..#.##.......#.##.......#.##.....",
        ".#.#.#....#.#.#.#....#.#.#.#....#",
        ".#........#.#........#.#........#",
        "#.##...#...#.##...#...#.##...#...",
        "#...##....##...##....##...##....#",
        ".#..#...#.#.#..#...#.#.#..##..#.#",
    ]
    assert count_trees(grid, 1, 3) == 14


if __name__ == "__main__":
    pytest.main([__file__])
