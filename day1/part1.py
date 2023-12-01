import os
import sys

def load_input():
    script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    f = open(f"{script_directory}/input.txt", "r")
    return f.read().split('\n')


def get_calibration_value(line):
    result = []

    for i in range(len(line)):
        if line[i].isdigit():
            result.append(line[i])
            break

    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit():
            result.append(line[i])
            break
    
    return int(''.join(result))


def execute():
    lines = load_input()
    calibration_values = list(map(get_calibration_value, lines))
    print(f"Sum={sum(calibration_values)}")


if __name__ == "__main__":
    execute()