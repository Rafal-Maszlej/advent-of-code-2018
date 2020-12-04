import pytest

from solver import Passport


@pytest.mark.parametrize("value", ["A", 20200, 123, 1919, 2003])
def test_birth_year_invalid_values(value, passport_data):
    passport_data["byr"] = value
    with pytest.raises(ValueError):
        Passport(**passport_data)


@pytest.mark.parametrize("value", ["A", 20200, 123, 2009, 2021])
def test_issue_year_invalid_values(value, passport_data):
    passport_data["iyr"] = value
    with pytest.raises(ValueError):
        Passport(**passport_data)


@pytest.mark.parametrize("value", ["A", 20200, 123, 2019, 2031])
def test_expiration_year_invalid_values(value, passport_data):
    passport_data["eyr"] = value
    with pytest.raises(ValueError):
        Passport(**passport_data)


@pytest.mark.parametrize("value", ["AAAAAA", 180, "180aa", "149cm", "194cm", "60aa", "58in", "77in"])
def test_height_invalid_values(value, passport_data):
    passport_data["hgt"] = value
    with pytest.raises(ValueError):
        Passport(**passport_data)


@pytest.mark.parametrize("value", ["A", 123, "A123456", "#12345", "#1234567", "#12345g"])
def test_hair_color_invalid_values(value, passport_data):
    passport_data["hcl"] = value
    with pytest.raises(ValueError):
        Passport(**passport_data)


@pytest.mark.parametrize("value", ["A", 123, "ab", "abcd", "asd"])
def test_eye_color_invalid_values(value, passport_data):
    passport_data["ecl"] = value
    with pytest.raises(ValueError):
        Passport(**passport_data)


@pytest.mark.parametrize("value", ["A", 123, "12345678", "1234567890", "a12345678"])
def test_passport_id_invalid_values(value, passport_data):
    passport_data["pid"] = value
    with pytest.raises(ValueError):
        Passport(**passport_data)


if __name__ == "__main__":
    pytest.main([__file__])
