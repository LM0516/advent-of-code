import numpy as np


def rotations(file_name):
    data = np.loadtxt(file_name, dtype=str, unpack=True)

    # Split string and number
    print(type(data))
    split_data = [(item[0], int(item[1:])) for item in data]

    return split_data


def part_one(data, value, count):
    for i in range(len(data)):
        match data[i][0]:
            case "L":
                value = (value - data[i][1]) % 100
            case "R":
                value = (value + data[i][1]) % 100

        if value == 0:
            count += 1

    print(count)


def main():
    file_name = "rotations.txt"
    data = rotations(file_name)
    value = 50
    count = 0

    part_one(data, value, count)


if __name__ == "__main__":
    main()
