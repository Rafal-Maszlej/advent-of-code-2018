def get_floor(data):
    return data.count("(") - data.count(")")


def get_basement_at(data):
    floor = 0

    for i in range(len(data)):
        if data[i] == "(":
            floor += 1
        elif data[i] == ")":
            floor -= 1

        if floor == -1:
            return i + 1


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().strip()

    #  Part 1
    assert get_floor(data) == 138

    #  Part 2
    assert get_basement_at(data) == 1771
