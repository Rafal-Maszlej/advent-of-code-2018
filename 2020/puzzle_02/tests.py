import pytest

from solver import get_schema_validator


@pytest.mark.parametrize(
    ["schema", "password"],
    [
        ("1-3 a", "abcde"),
        ("2-9 c", "ccccccccc")
    ]
)
def test_old_schema_password_validation_success(schema, password):
    validator = get_schema_validator(schema)
    assert validator.validate_password_old(password) is True


def test_old_schema_password_validation_failed():
    validator = get_schema_validator("1-3 b")
    password = "cdefg"
    assert validator.validate_password_old(password) is False


def test_schema_password_validation_success():
    validator = get_schema_validator("1-3 a")
    password = "abcde"
    assert validator.validate_password(password) is True


@pytest.mark.parametrize(
    ["schema", "password"],
    [
        ("1-3 b", "cdefg"),
        ("2-9 c", "ccccccccc")
    ]
)
def test_schema_password_validation_failed(schema, password):
    validator = get_schema_validator(schema)
    assert validator.validate_password(password) is False


if __name__ == "__main__":
    pytest.main([__file__])
