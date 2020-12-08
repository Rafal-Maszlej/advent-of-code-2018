import pytest

from solver import Interpreter, ResultCode


@pytest.fixture
def interpreter():
    return Interpreter()


@pytest.fixture
def program():
    return """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6""".split("\n")


def test_acc(interpreter):
    interpreter.acc_op(5)
    assert interpreter.accumulator == 5
    assert interpreter.instruction_pointer == 1

    interpreter.acc_op(-3)
    assert interpreter.accumulator == 2
    assert interpreter.accumulator == 2


def test_jmp(interpreter):
    interpreter.jmp_op(20)
    assert interpreter.instruction_pointer == 20

    interpreter.jmp_op(-5)
    assert interpreter.instruction_pointer == 15
    assert interpreter.accumulator == 0


def test_nop(interpreter):
    interpreter.nop_op()
    assert interpreter.accumulator == 0
    assert interpreter.instruction_pointer == 1


def test_load(interpreter, program):
    interpreter.load(program)
    assert len(interpreter.instructions) == 9
    assert interpreter.instructions[0] == ("nop", 0)
    assert interpreter.instructions[2] == ("jmp", 4)
    assert interpreter.instructions[5] == ("acc", -99)


def test_run(interpreter, program):
    interpreter.load(program)
    result = interpreter.run()
    assert result.value == 5


def test_debug(interpreter, program):
    result = interpreter.debug(program)
    assert result.value == 8
    assert result.code == ResultCode.OK


if __name__ == "__main__":
    pytest.main([__file__])
