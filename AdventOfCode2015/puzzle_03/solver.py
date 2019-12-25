def coords_calc(data):
    coords_mapping = {
        "^": (0, 1),
        "v": (0, -1),
        ">": (1, 0),
        "<": (-1, 0)
    }
    current_coords = (0, 0)
    coordinates = set()

    coordinates.add(current_coords)

    for char in data:
        coords_delta = coords_mapping[char]
        current_coords = (current_coords[0] + coords_delta[0], current_coords[1] + coords_delta[1])
        coordinates.add(current_coords)

    return coordinates


def coords_calc_splited_data(data):
    data_1 = data[::2]
    data_2 = data[1::2]

    coords_1 = coords_calc(data_1)
    coords_2 = coords_calc(data_2)

    return coords_1.union(coords_2)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().strip()

    #  Part 1
    assert len(coords_calc(data)) == 2572

    #  Part 2
    assert len(coords_calc_splited_data(data)) == 2631
