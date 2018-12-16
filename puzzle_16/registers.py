class Opcodes:
    @classmethod
    def op_addr(cls, registers, a, b, c):
        registers[c].value = registers[a].value + registers[b].value

    @classmethod
    def op_addi(cls, registers, a, b, c):
        registers[c].value = registers[a].value + b

    @classmethod
    def op_mulr(cls, registers, a, b, c):
        registers[c].value = registers[a].value * registers[b].value

    @classmethod
    def op_muli(cls, registers, a, b, c):
        registers[c].value = registers[a].value * b

    @classmethod
    def op_banr(cls, registers, a, b, c):
        registers[c].value = registers[a].value & registers[b].value

    @classmethod
    def op_bani(cls, registers, a, b, c):
        registers[c].value = registers[a].value & b

    @classmethod
    def op_borr(cls, registers, a, b, c):
        registers[c].value = registers[a].value | registers[b].value

    @classmethod
    def op_bori(cls, registers, a, b, c):
        registers[c].value = registers[a].value | b

    @classmethod
    def op_setr(cls, registers, a, b, c):
        registers[c].value = registers[a].value

    @classmethod
    def op_seti(cls, registers, a, b, c):
        registers[c].value = a

    @classmethod
    def op_gtir(cls, registers, a, b, c):
        registers[c].value = (0, 1)[a > registers[b].value]

    @classmethod
    def op_gtri(cls, registers, a, b, c):
        registers[c].value = (0, 1)[registers[a].value > b]

    @classmethod
    def op_gtrr(cls, registers, a, b, c):
        registers[c].value = (0, 1)[registers[a].value > registers[b].value]

    @classmethod
    def op_eqir(cls, registers, a, b, c):
        registers[c].value = (0, 1)[a == registers[b].value]

    @classmethod
    def op_eqri(cls, registers, a, b, c):
        registers[c].value = (0, 1)[registers[a].value == b]

    @classmethod
    def op_eqrr(cls, registers, a, b, c):
        registers[c].value = (0, 1)[registers[a].value == registers[b].value]


class Register:
    def __init__(self, id, value=0):
        self.id = id
        self.value = value

    def __repr__(self):
        return f"<Register id: {self.id} value: {self.value}>"
