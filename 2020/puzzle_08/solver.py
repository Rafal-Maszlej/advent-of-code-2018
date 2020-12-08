from collections import namedtuple
from enum import Enum
from typing import List


Instruction = namedtuple("INS", ["code", "value"])
Result = namedtuple("RESULT", ["code", "value"])


class ResultCode(Enum):
    OK = 0
    BREAK = 1


class Interpreter:
    def __init__(self, accumulator=0, pointer=0):
        self.accumulator = accumulator
        self.instruction_pointer = pointer
        self.instructions = []
        self.instructions_history = []

    def acc_op(self, value):
        self.accumulator += value
        self.instruction_pointer += 1

    def jmp_op(self, value):
        self.instruction_pointer += value

    def nop_op(self, *args):
        self.instruction_pointer += 1

    def get_opp(self, code: str):
        return {
            "acc": self.acc_op,
            "jmp": self.jmp_op,
            "nop": self.nop_op
        }.get(code)

    def load(self, data: List[str]):
        for row in data:
            code, value = row.strip().split(" ")
            value = int(value)
            instruction = Instruction(code, value)
            self.instructions.append(instruction)

    def reset(self):
        self.accumulator = 0
        self.instruction_pointer = 0
        self.instructions = []
        self.instructions_history = []

    def run(self):
        while self.instruction_pointer < len(self.instructions):
            if self.instruction_pointer in self.instructions_history:
                return Result(code=ResultCode.BREAK, value=self.accumulator)

            instruction = self.instructions[self.instruction_pointer]
            self.instructions_history.append(self.instruction_pointer)

            operation = self.get_opp(instruction.code)
            operation(instruction.value)

        return Result(code=ResultCode.OK, value=self.accumulator)

    def debug(self, program: List[str]):
        for index in range(len(program)):
            instruction = program[index]

            if "jmp" in instruction:
                code, value = instruction.split(" ")
                debug_instruction = f"nop {value}"
                debug_program = program.copy()
                debug_program[index] = debug_instruction
            elif "nop" in instruction:
                code, value = instruction.split(" ")
                debug_instruction = f"jmp {value}"
                debug_program = program.copy()
                debug_program[index] = debug_instruction
            else:
                continue

            self.reset()
            self.load(debug_program)
            result = self.run()

            if result.code == ResultCode.OK:
                return result


if __name__ == "__main__":
    with open("input.txt") as f:
        program = f.readlines()

    interpreter = Interpreter()
    interpreter.load(program)

    # puzzle 1
    result = interpreter.run()
    assert result.value == 1766

    # puzzle 2
    result = interpreter.debug(program)
    assert result.value == 1639
