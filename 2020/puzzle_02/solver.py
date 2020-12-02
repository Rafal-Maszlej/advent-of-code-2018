from dataclasses import dataclass


class PasswordValidationError(Exception):
    ...


@dataclass
class PasswordSchemaValidator:
    letter: str
    index_low: int
    index_high: int

    @staticmethod
    def get_letter(index, password):
        try:
            return password[index - 1]
        except IndexError:
            return

    @staticmethod
    def validate_different_letters(letter_1, letter_2):
        if letter_1 == letter_2:
            raise PasswordValidationError

    def validate_password_letter(self, letter_1, letter_2):
        if self.letter not in [letter_1, letter_2]:
            raise PasswordValidationError

    def validate_password(self, password):
        first_letter = self.get_letter(self.index_low, password)
        second_letter = self.get_letter(self.index_high, password)

        try:
            self.validate_different_letters(first_letter, second_letter)
            self.validate_password_letter(first_letter, second_letter)
            return True
        except PasswordValidationError:
            return False

    def validate_password_old(self, password):
        return self.index_low <= password.count(self.letter) <= self.index_high


def get_schema_validator(schema):
    schema, letter = schema.split()
    index_low, index_high = [int(number) for number in schema.split("-")]
    return PasswordSchemaValidator(
        letter=letter,
        index_low=index_low,
        index_high=index_high
    )


def parse_data(data):
    data = [row.strip().split(": ") for row in data]
    return [[get_schema_validator(schema), password] for schema, password in data]


if __name__ == "__main__":
    with open("input.txt") as f:
        data = parse_data(f.readlines())

    # puzzle 1
    assert sum([schema.validate_password_old(password) for schema, password in data]) == 424

    # puzzle 2
    assert sum([schema.validate_password(password) for schema, password in data]) == 747
