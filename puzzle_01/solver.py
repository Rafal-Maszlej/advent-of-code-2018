from itertools import cycle


def find_frequency(puzzle_input):
    frequencies = [0]
    
    for i in cycle(puzzle_input):
        frequency = frequencies[-1] + i
        
        if frequency in frequencies:
            return frequency
    
        frequencies.append(frequency)


if __name__ == '__main__':
    puzzle_input = [int(i) for i in open('input.txt').readlines()]
    
    # part 1
    assert sum(puzzle_input) == 416
    
    # part 2
    assert find_frequency([1, -1]) == 0
    assert find_frequency([3, 3, 4, -2, -4]) == 10
    assert find_frequency([-6, 3, 8, 5, -6]) == 5
    assert find_frequency([7, 7, -2, -7, -4]) == 14
    assert find_frequency([1, -2, 3, 1]) == 2

    assert find_frequency(puzzle_input) == 56752
