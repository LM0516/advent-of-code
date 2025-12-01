import numpy as np


def rotations(file_name):
    data = np.loadtxt(file_name, dtype=str, unpack=True)

    # Split string and number
    print(type(data))
    split_data = [(item[0], int(item[1:])) for item in data]

    return split_data


def main():
    file_name = "rotations.txt"
    data = rotations(file_name)
    value = 50
    count = 0

    for i in range(len(data)):
        if value == 0:
            count += 1

        match data[i][0]:
            case "L":
                value -= data[i][1]
                if value < 0:
                    value = 100 + value
            case "R":
                value += data[i][1]
                if value > 99:
                    value = value - 100

    print(count)


if __name__ == "__main__":
    main()
