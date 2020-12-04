import pytest


@pytest.fixture
def passport_data():
    return {
        "byr": "1937",
        "iyr": "2017",
        "eyr": "2020",
        "hgt": "183cm",
        "hcl": "#fffffd",
        "ecl": "gry",
        "pid": "860033327",
        "cid": "147"
    }


@pytest.fixture
def invalid_passport_data():
    return {
        "byr": "1937",
        "iyr": "2017",
        "eyr": "2020",
        "hgt": "183cm",
        "hcl": "#fffffd",
        "ecl": "gry",
        "cid": "147"
    }


@pytest.fixture
def raw_passports_data():
    return """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
""".strip()
