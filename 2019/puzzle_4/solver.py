from string import digits


if __name__ == "__main__":
    input_range = range(387638, 919123 + 1)

    counter = 0

    for p in input_range:
        password = str(p)

        #  Part 1
        if not all(password[i-1] <= password[i] for i in range(1, 6)):
            continue

        if not any(password[i-1] == password[i] for i in range(1, 6)):
            continue

        #  Part 2
        slices = [password[i-2:i] for i in range(2, 7)]

        if 1 not in [slices.count(i) for i in [d*2 for d in digits]]:
            continue

        counter += 1

    print(counter)
