from typing import List


def prepare_data(data):
    data.append(0)
    data.sort()
    data.append(data[-1] + 3)
    return data


def joltage_difference(data: List[int]):
    data = prepare_data(data)

    diff_1 = [data[i] for i in range(1, len(data)) if data[i] - data[i-1] == 1]
    diff_3 = [data[i] for i in range(1, len(data)) if data[i] - data[i-1] == 3]

    return len(diff_1) * len(diff_3)


def combinations_count(data: List[int]):
    data = prepare_data(data)

    breakpoint()


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [int(i) for i in f.readlines()]

    # puzzle 1
    assert joltage_difference(data) == 2312

    # puzzle 2

