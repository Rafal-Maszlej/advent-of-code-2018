from core import IntcodeComputer


if __name__ == "__main__":
    with open("input.txt") as f:
        _program = [int(i) for i in f.read().strip().split(",")]

    computer = IntcodeComputer()

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
