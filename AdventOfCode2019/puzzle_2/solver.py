class Computer:
    OP_ADD = 1
    OP_MUL = 2
    OP_END = 99

    def __init__(self):
        self.memory = []

    def load_program(self, program: list):
        self.memory = program

    def op_add(self, param1, param2, param3):
        self.memory[param3] = self.memory[param1] + self.memory[param2]

    def op_mul(self, param1, param2, param3):
        self.memory[param3] = self.memory[param1] * self.memory[param2]

    def run(self):
        if not self.memory or self.OP_END not in self.memory:
            return

        instruction_pointer = 0

        while True:
            if self.memory[instruction_pointer] == self.OP_ADD:
                self.op_add(
                    param1=self.memory[instruction_pointer + 1],
                    param2=self.memory[instruction_pointer + 2],
                    param3=self.memory[instruction_pointer + 3]
                )
                instruction_pointer += 3
            elif self.memory[instruction_pointer] == self.OP_MUL:
                self.op_mul(
                    param1=self.memory[instruction_pointer + 1],
                    param2=self.memory[instruction_pointer + 2],
                    param3=self.memory[instruction_pointer + 3]
                )
                instruction_pointer += 3
            elif self.memory[instruction_pointer] == self.OP_END:
                return self.memory[0]
            else:
                instruction_pointer += 1


if __name__ == "__main__":
    with open("input.txt") as f:
        _program = [int(i) for i in f.read().strip().split(",")]

    computer = Computer()

    #  Part 1
    program = _program.copy()
    program[1] = 12
    program[2] = 2

    computer.load_program(program)
    result = computer.run()

    assert result == 2894520

    #  Part 2
    expected_result = 19690720
    part_2_answer = None

    for noun in range(99):
        for verb in range(99):
            program = _program.copy()
            program[1] = noun
            program[2] = verb

            computer.load_program(program)

            try:
                result = computer.run()
                if result == expected_result:
                    part_2_answer = 100 * noun + verb
            except IndexError:
                pass

    assert part_2_answer == 9342
