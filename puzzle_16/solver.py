from registers import Opcodes, Register, ReverseOpcodeBase
from parsers import InputParser


class ReverseOpcodes(ReverseOpcodeBase):
    def __init__(self, input_instructions_file):
        super().__init__()
        self.parser = InputParser(input_instructions_file)

    def run_test_instruction(self):
        instruction, registers_before, registers_after = self.parser.get_test_case()
        opcode_id, *instruction = instruction
        results = [self.is_valid_opcode(opcode, instruction, registers_before, registers_after) for opcode in self.opcodes]

        return sum(results) >= 3

    def run(self):
        result = 0

        while self.parser.data:
            result += self.run_test_instruction()

        return result


class ReverseOpcodeMapping(ReverseOpcodeBase):
    def __init__(self, input_instructions_file):
        super().__init__()
        self.parser = InputParser(input_instructions_file)

    def run_test_instruction(self):
        instruction, registers_before, registers_after = self.parser.get_test_case()
        opcode_id, *instruction = instruction
        return opcode_id, [opcode for opcode in self.opcodes if self.is_valid_opcode(opcode, instruction, registers_before, registers_after)]

    def get_possible_opcode_mapping(self):
        mapping = {opcode: set() for opcode in dir(Opcodes) if opcode.startswith('op_')}

        while self.parser.data:
            opcode_id, valid_opcodes = self.run_test_instruction()

            for opcode in valid_opcodes:
                mapping[opcode].add(opcode_id)

        return mapping

    def find_opcode_mapping(self):
        _mapping = self.get_possible_opcode_mapping()

        mapping = {}

        while _mapping:
            for opcode, values in _mapping.items():
                if len(values) == 1:
                    opcode_id = values.pop()
                    mapping[opcode_id] = getattr(Opcodes, opcode)
                    _mapping.pop(opcode)
                    break

            for opcode in _mapping:
                if opcode_id in _mapping[opcode]:
                    _mapping[opcode].remove(opcode_id)

        return mapping


class ProgramRunner:
    opcodes = {
        0: Opcodes.op_mulr,
        1: Opcodes.op_addr,
        2: Opcodes.op_banr,
        3: Opcodes.op_eqir,
        4: Opcodes.op_muli,
        5: Opcodes.op_setr,
        6: Opcodes.op_eqri,
        7: Opcodes.op_gtri,
        8: Opcodes.op_eqrr,
        9: Opcodes.op_addi,
        10: Opcodes.op_gtir,
        11: Opcodes.op_gtrr,
        12: Opcodes.op_borr,
        13: Opcodes.op_bani,
        14: Opcodes.op_seti,
        15: Opcodes.op_bori,
    }

    def __init__(self, input_program_file):
        self.parser = InputParser(input_program_file)
        self.registers = [Register(i) for i in range(4)]

    def run(self):
        while self.parser.data:
            opcode_id, a, b, c = self.parser.get_line()

            self.opcodes[opcode_id](self.registers, a, b, c)


if __name__ == '__main__':
    # part 1
    assert ReverseOpcodes('input_instructions.txt').run() == 663

    # part 2
    assert ReverseOpcodeMapping('input_instructions.txt').find_opcode_mapping() == {
        0: Opcodes.op_mulr,
        1: Opcodes.op_addr,
        2: Opcodes.op_banr,
        3: Opcodes.op_eqir,
        4: Opcodes.op_muli,
        5: Opcodes.op_setr,
        6: Opcodes.op_eqri,
        7: Opcodes.op_gtri,
        8: Opcodes.op_eqrr,
        9: Opcodes.op_addi,
        10: Opcodes.op_gtir,
        11: Opcodes.op_gtrr,
        12: Opcodes.op_borr,
        13: Opcodes.op_bani,
        14: Opcodes.op_seti,
        15: Opcodes.op_bori,
    }

    program = ProgramRunner('input_program.txt')
    program.run()

    assert program.registers[0].value == 525
