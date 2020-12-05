from dataclasses import dataclass
from math import ceil, floor


@dataclass
class Zone:
    min_row: int = 0
    max_row: int = 127
    min_col: int = 0
    max_col: int = 7

    def front(self):
        difference = self.max_row - self.min_row
        self.max_row = self.min_row + floor(difference / 2)

    def back(self):
        difference = self.max_row - self.min_row
        self.min_row += ceil(difference / 2)

    def right(self):
        difference = self.max_col - self.min_col
        self.min_col += ceil(difference / 2)

    def left(self):
        difference = self.max_col - self.min_col
        self.max_col = self.min_col + floor(difference / 2)

    def nop(self):
        ...

    def get_action(self, code):
        actions = {
            "F": self.front,
            "B": self.back,
            "R": self.right,
            "L": self.left
        }
        return actions.get(code, self.nop)

    def update(self, code: str):
        action = self.get_action(code)
        action()


def get_seat_id(boarding_pass: str) -> int:
    zone = Zone()

    for code in boarding_pass:
        zone.update(code)

    return zone.max_row * 8 + zone.max_col


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [row.strip() for row in f.readlines()]

    # puzzle 1
    seat_ids = [get_seat_id(boarding_pass) for boarding_pass in data]
    assert max(seat_ids) == 871

    # puzzle 2
    seat_ids = sorted(seat_ids)
    missing_ids_set = set(range(seat_ids[0], seat_ids[-1] + 1)).difference(set(seat_ids))
    assert missing_ids_set == {640}
