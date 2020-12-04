from pydantic import BaseModel, PositiveInt, validator
from typing import Dict, List, Optional


class Passport(BaseModel):
    byr: PositiveInt
    iyr: PositiveInt
    eyr: PositiveInt
    hgt: str
    hcl: str
    ecl: str
    pid: str
    cid: Optional[PositiveInt]

    @validator("byr")
    def validate_birth_year(cls, byr):
        if not 1920 <= byr <= 2002:
            raise ValueError("Wrong birth year")

    @validator("iyr")
    def validate_issue_year(cls, iyr):
        if not 2010 <= iyr <= 2020:
            raise ValueError("Wrong issue year")

    @validator("eyr")
    def validate_expiration_year(cls, eyr):
        if not 2020 <= eyr <= 2030:
            raise ValueError("Wrong expiration year")

    @validator("hgt")
    def validate_height(cls, hgt):
        error_message = "Wrong height"

        height, metric = hgt[:-2], hgt[-2:]

        if metric not in ["cm", "in"]:
            raise ValueError(error_message)

        if not height.isdigit():
            raise ValueError(error_message)

        height = int(height)

        if metric == "cm":
            if not 150 <= height <= 193:
                raise ValueError(error_message)
        elif metric == "in":
            if not 59 <= height <= 76:
                raise ValueError(error_message)

    @validator("hcl")
    def validate_hair_color(cls, hcl):
        error_message = "Wrong hair color"

        if not hcl.startswith("#"):
            raise ValueError(error_message)

        color = hcl[1:]

        if not len(color) == 6:
            raise ValueError(error_message)

        try:
            int(color, base=16)
        except ValueError:
            raise ValueError(error_message)

    @validator("ecl")
    def validate_eye_color(cls, ecl):
        valid_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

        if ecl not in valid_colors:
            raise ValueError("Wrong eye color")

    @validator("pid")
    def validate_passport_id(cls, pid):
        if not pid.isdigit() or len(pid) != 9:
            raise ValueError("Wrong passport ID")


def parse_data(data: str) -> List[Dict]:
    raw_passports_data = data.strip().split("\n\n")
    data = []

    for raw_data in raw_passports_data:
        passport_data = dict([element.split(":") for element in raw_data.replace("\n", " ").split()])
        data.append(passport_data)

    return data


def get_passports(data: List[Dict]) -> List[Passport]:
    passports = []

    for passport_data in data:
        try:
            passports.append(Passport(**passport_data))
        except ValueError:
            pass

    return passports


if __name__ == "__main__":
    with open("input.txt") as f:
        raw_data = f.read()

    data = parse_data(raw_data)
    passports = get_passports(data)

    # puzzle 1
    # doesn't work anymore because of fields validation
    # assert len(passports) == 233

    # puzzle 2
    assert len(passports) == 111
