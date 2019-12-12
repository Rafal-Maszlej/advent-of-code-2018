class IntcodeComputer:
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
