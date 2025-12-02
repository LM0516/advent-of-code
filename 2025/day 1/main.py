import numpy as np


def rotations(file_name):
    data = np.loadtxt(file_name, dtype=str, unpack=True)
    data = [int(d.replace("R", "").replace("L", "-")) for d in data]

    return data


def part_one(data, value, count):
    for d in data:
        value = (value + d) % 100
        if value == 0:
            count += 1

    print(count)


def part_two(data, value, count):
    laps = []
    for d in data:
        # lap, value = value // d % 100
        lap, value = divmod(value + d, 100)
        print(f"{abs(lap)} - {value}")
        laps.append(abs(lap))
        if value == 0:
            count += 1

    print(count + sum(laps))


def main():
    file_name = "rotations.txt"
    data = rotations(file_name)
    value = 50
    count = 0

    print("=== Part One ===")
    part_one(data, value, count)
    print("=== Part Two ===")
    part_two(data, value, count)


if __name__ == "__main__":
    main()
