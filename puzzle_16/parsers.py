class InputParser:
    def __init__(self, file_path):
        self.data = self.read(file_path)

    def read(self, file_path):
        with open(file_path) as f:
            return list(reversed(f.readlines()))

    def parse_registers_before(self):
        return [int(value) for value in self.data.pop().strip().replace(' ', '').strip('Before:[]').split(',')]

    def parse_registers_after(self):
        return [int(value) for value in self.data.pop().strip().replace(' ', '').strip('After:[]').split(',')]

    def parse_instrucion(self):
        return [int(value) for value in self.data.pop().strip().split()]

    def get_test_case(self):
        registers_before = self.parse_registers_before()
        instruction = self.parse_instrucion()
        registers_after = self.parse_registers_after()

        if self.data:
            self.data.pop()

        return instruction, registers_before, registers_after

    def get_line(self):
        return [int(value) for value in self.data.pop().strip().split()]
