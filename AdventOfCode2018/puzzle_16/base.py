from parsers import InputParser
from registers import Opcodes, Register


class ReverseOpcodeBase:
    def __init__(self, input_file):
        self.registers = [Register(i) for i in range(4)]
        self.opcodes = [opcode for opcode in dir(Opcodes) if opcode.startswith('op_')]
        self.parser = InputParser(input_file)

    def assign_registers(self, values):
        for register, value in zip(self.registers, values):
            register.value = value

    def compare_registers(self, values):
        return all(register.value == value for register, value in zip(self.registers, values))

    def is_valid_opcode(self, opcode, instruction, registers_before, registers_after):
        self.assign_registers(registers_before)
        getattr(Opcodes, opcode)(self.registers, *instruction)

        return self.compare_registers(registers_after)
