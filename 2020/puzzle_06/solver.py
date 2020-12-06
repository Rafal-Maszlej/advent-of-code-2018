from functools import reduce


if __name__ == "__main__":
    BLANK_LINE = "\n\n"

    with open("input.txt") as f:
        data = f.read().split(BLANK_LINE)

    # puzzle 1
    unique_answers = [set(answers.replace("\n", "")) for answers in data]
    unique_answers_sum = sum([len(answers) for answers in unique_answers])
    assert unique_answers_sum == 6768

    # puzzle 2
    all_answers = [[set(a) for a in answers.split("\n")] for answers in data]
    same_answers = [reduce(lambda a, b: a.intersection(b), answers) for answers in all_answers]
    same_answers_sum = sum([len(answers) for answers in same_answers])
    assert same_answers_sum == 3489
