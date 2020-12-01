from itertools import combinations
from functools import reduce


def find_multiplication(numbers, amount, total_sum):
    for n in combinations(numbers, amount):
        if sum(n) == total_sum:
            return reduce(lambda x, y: x * y, n)


if __name__ == "__main__":
    numbers = [1721, 979, 366, 299, 675, 1456]
    total_sum = 2020

    assert find_multiplication(numbers, 2, total_sum) == 514579
    assert find_multiplication(numbers, 3, total_sum) == 241861950

    with open("input.txt") as f:
        numbers = [int(n) for n in f.readlines()]

    # puzzle 1
    print(find_multiplication(numbers, 2, total_sum))

    # puzzle 2
    print(find_multiplication(numbers, 3, total_sum))
