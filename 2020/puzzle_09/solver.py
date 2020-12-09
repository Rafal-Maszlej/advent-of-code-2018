from typing import List


def find_first_invalid_number(data: List[int], preamble: int) -> int:
    for i in range(0, len(data) - preamble):
        numbers = data[i:i + preamble]

        valid_numbers = []
        number = data[i + preamble]

        for x in numbers:
            y = number - x

            if y != x and y in numbers:
                valid_numbers.append(x)

        if not valid_numbers:
            return number


def find_contiguous_numbers(data: List[int], number: int) -> List[int]:
    for n in range(2, len(data)):
        for i in range(len(data) + 1 - n):
            numbers = data[i:i + n]

            if sum(numbers) == number:
                return numbers


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [int(line.strip()) for line in f.readlines()]

    # puzzle 1
    invalid_number = find_first_invalid_number(data, preamble=25)
    assert invalid_number == 1504371145

    # puzzle 2
    numbers = find_contiguous_numbers(data, number=invalid_number)
    numbers.sort()
    encryption_key = numbers[0] + numbers[-1]
    assert encryption_key == 183278487
