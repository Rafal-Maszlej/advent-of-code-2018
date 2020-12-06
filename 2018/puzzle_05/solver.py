from string import ascii_lowercase, ascii_uppercase


def react(data):
    pairs = [i + j for i, j in zip(ascii_lowercase + ascii_uppercase, ascii_uppercase + ascii_lowercase)]

    while data:
        for pair in pairs:
            if data.find(pair) != -1:
                data = data.replace(pair, '')
                break
        else:
            return len(data)


def solver2(data):
    reactions = {
        unit: react(data.replace(unit, '').replace(unit.upper(), ''))
        for unit in ascii_lowercase
    }

    return min(reactions.values())


if __name__ == '__main__':
    with open("input.txt") as f:
        data = f.read().strip()

    # solution1
    answer = react(data)
    assert answer == 9386

    # solution2
    answer = solver2(data)
    assert answer == 4876

    # tests

    test_data = "dabAcCaCBAcCcaDA"

    assert react(test_data) == len("dabCBAcaDA")
    assert solver2(test_data) == 4
