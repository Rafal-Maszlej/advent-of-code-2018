import pytest

from solver import Computer


@pytest.fixture
def program():
    return [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]


@pytest.fixture
def computer(program):
    computer = Computer()
    computer.load_program(program)
    return computer


def test_op_add(computer):
    expected_memory = [1, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
    computer.op_add(9, 10, 3)

    assert computer.memory == expected_memory


def test_op_mul(computer):
    expected_memory = [150, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
    computer.op_mul(3, 11, 0)

    assert computer.memory == expected_memory


def test_run_program1(computer):
    program = [1, 0, 0, 0, 99]
    expected_memory = [2, 0, 0, 0, 99]
    computer.load_program(program)
    computer.run()

    assert computer.memory == expected_memory


def test_run_program2(computer):
    program = [2, 3, 0, 3, 99]
    expected_memory = [2, 3, 0, 6, 99]
    computer.load_program(program)
    computer.run()

    assert computer.memory == expected_memory


def test_run_program3(computer):
    program = [2, 4, 4, 5, 99, 0]
    expected_memory = [2, 4, 4, 5, 99, 9801]
    computer.load_program(program)
    computer.run()

    assert computer.memory == expected_memory


def test_run_program4(computer):
    program = [1, 1, 1, 4, 99, 5, 6, 0, 99]
    expected_memory = [30, 1, 1, 4, 2, 5, 6, 0, 99]
    computer.load_program(program)
    computer.run()

    assert computer.memory == expected_memory


if __name__ == "__main__":
    pytest.main([__file__])
