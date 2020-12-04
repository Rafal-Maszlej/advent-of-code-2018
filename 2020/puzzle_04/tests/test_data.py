import pytest

from solver import Passport, parse_data, get_passports


def test_create_passport(passport_data):
    passport = Passport(**passport_data)
    assert passport is not None


def test_create_passport_cid_optional(passport_data):
    passport_data.pop("cid")
    passport = Passport(**passport_data)
    assert passport is not None


@pytest.mark.parametrize("field", ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
def test_create_passport_required_field(field, passport_data):
    passport_data.pop(field)
    with pytest.raises(ValueError):
        Passport(**passport_data)


def test_parse_data(raw_passports_data):
    passports_data = parse_data(raw_passports_data)
    assert len(passports_data) == 4

    passport = passports_data[0]
    assert passport.get("ecl") == "gry"
    assert passport.get("pid") == "860033327"
    assert passport.get("hcl") == "#fffffd"


def test_get_passports(passport_data):
    passports = get_passports([passport_data])
    assert len(passports) == 1
    assert isinstance(passports[0], Passport)


def test_get_passports_invalid_data(passport_data, invalid_passport_data):
    data = [passport_data, invalid_passport_data]
    passports = get_passports(data)
    assert len(passports) == 1


def test_integration(raw_passports_data):
    data = parse_data(raw_passports_data)
    passports = get_passports(data)
    assert len(passports) == 2


if __name__ == "__main__":
    pytest.main([__file__])
