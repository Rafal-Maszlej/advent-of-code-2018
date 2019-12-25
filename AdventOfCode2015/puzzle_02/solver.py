def get_dimensions(data):
    return [int(i) for i in data.strip().split("x")]


def get_paper_surface(data):
    l, w, h = get_dimensions(data)

    area_1 = l * w
    area_2 = w * h
    area_3 = h * l

    return 2 * sum([area_1, area_2, area_3]) + min(area_1, area_2, area_3)


def get_ribbon_length(data):
    l, w, h = get_dimensions(data)

    min_a, min_b = sorted([l, w, h])[:2]

    return 2 * min_a + 2 * min_b + l * w * h


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().strip()

    #  Part 1
    total_paper_surface = sum([get_paper_surface(square) for square in data.split("\n")])
    assert total_paper_surface == 1586300

    #  Part 2
    total_ribbon_length = sum([get_ribbon_length(square) for square in data.split("\n")])
    assert total_ribbon_length == 3737498
