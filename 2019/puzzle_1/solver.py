def calculate_fuel(mass):
    return mass // 3 - 2


def calculate_total_module_fuel(mass):
    fuel = calculate_fuel(mass)

    if fuel <= 0:
        return 0

    return fuel + calculate_total_module_fuel(fuel)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [int(i.strip()) for i in f.readlines()]

    #  Part 1
    total_fuel = sum(calculate_fuel(mass) for mass in data)
    print(total_fuel)

    #  Part 2
    total_fuel = sum(calculate_total_module_fuel(mass) for mass in data)
    print(total_fuel)
