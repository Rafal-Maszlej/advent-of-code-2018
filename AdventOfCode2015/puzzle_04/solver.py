from hashlib import md5


def advent_coin_calculate(data, number_of_zeroes=5):
    number = 1

    while True:
        number += 1
        md5_hash = md5((data + str(number)).encode()).hexdigest()

        if md5_hash.startswith("0" * number_of_zeroes):
            return number


if __name__ == "__main__":
    data = "bgvyzdsv"

    #  Part 1
    assert advent_coin_calculate(data) == 254575

    #  Part 2
    assert advent_coin_calculate(data, number_of_zeroes=6) == 1038736
