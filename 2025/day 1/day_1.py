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

    for i in range(len(data)):
        match data[i][0]:
            case "L":
                print("Left:")
                print(data[i][1])
            case "R":
                print("Right:")
                print(data[i][1])


if __name__ == "__main__":
    main()
